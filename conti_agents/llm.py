"""Thin wrapper around the Claude API: run a short agent loop until Claude calls a 'submit' tool.

Each agent gets a system prompt, some content (text, PDF, images) and an output JSON schema.
Optionally it also gets Anthropic's server-side web_search / web_fetch tools, which run on
Anthropic's side - no SSRN API key or scraper is needed.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any

import jsonschema

log = logging.getLogger(__name__)


class AgentError(RuntimeError):
    pass


def web_search_tool(max_uses: int, allowed_domains: list[str] | None = None) -> dict:
    tool = {"type": "web_search_20250305", "name": "web_search", "max_uses": max_uses}
    if allowed_domains:
        tool["allowed_domains"] = allowed_domains
    return tool


def web_fetch_tool(max_uses: int, allowed_domains: list[str] | None = None) -> dict:
    tool = {"type": "web_fetch_20250910", "name": "web_fetch", "max_uses": max_uses}
    if allowed_domains:
        tool["allowed_domains"] = allowed_domains
    return tool


@dataclass
class Usage:
    input_tokens: int = 0
    output_tokens: int = 0
    calls: int = 0
    by_agent: dict = field(default_factory=dict)

    def add(self, agent: str, usage: Any) -> None:
        i = getattr(usage, "input_tokens", 0) or 0
        i += (getattr(usage, "cache_read_input_tokens", 0) or 0) + (getattr(usage, "cache_creation_input_tokens", 0) or 0)
        o = getattr(usage, "output_tokens", 0) or 0
        self.input_tokens += i
        self.output_tokens += o
        self.calls += 1
        a = self.by_agent.setdefault(agent, {"input_tokens": 0, "output_tokens": 0, "calls": 0})
        a["input_tokens"] += i
        a["output_tokens"] += o
        a["calls"] += 1


class ClaudeLLM:
    def __init__(self, client=None):
        if client is None:
            import anthropic
            client = anthropic.Anthropic(max_retries=4)
        self.client = client
        self.usage = Usage()
        self.no_forced_tool: set[str] = set()   # models that reject tool_choice type "tool"

    def _create(self, kwargs: dict):
        # Streaming avoids HTTP timeouts on long PDF reads.
        with self.client.messages.stream(**kwargs) as stream:
            return stream.get_final_message()

    def structured(self, *, agent: str, model: str, system: str, content: Any, tool_name: str,
                   schema: dict, server_tools: list[dict] | None = None,
                   max_tokens: int = 16000, max_turns: int = 8) -> dict:
        tools = list(server_tools or []) + [{
            "name": tool_name,
            "description": "Submit your final result. Call this exactly once, when you are done.",
            "input_schema": schema,
        }]
        system_blocks = [{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}]
        reminder = {"type": "text", "text": f"When you are done, call the {tool_name} tool with your result."}
        content = ([{"type": "text", "text": content}] if isinstance(content, str) else list(content)) + [reminder]
        messages: list[dict] = [{"role": "user", "content": content}]
        force = not server_tools

        for turn in range(max_turns):
            kwargs = dict(model=model, max_tokens=max_tokens, system=system_blocks,
                          messages=messages, tools=tools)
            if (force or turn == max_turns - 1) and model not in self.no_forced_tool:
                kwargs["tool_choice"] = {"type": "tool", "name": tool_name}
            try:
                resp = self._create(kwargs)
            except Exception as e:  # some models (e.g. with thinking on by default) reject forced tool use
                if "tool_choice" in kwargs and "tool_choice" in str(e) and "not supported" in str(e):
                    log.info("%s does not support forced tool_choice; asking for the tool call instead", model)
                    self.no_forced_tool.add(model)
                    kwargs.pop("tool_choice")
                    resp = self._create(kwargs)
                else:
                    raise
            self.usage.add(agent, resp.usage)

            for block in resp.content:
                if getattr(block, "type", None) == "tool_use" and block.name == tool_name:
                    result = dict(block.input)
                    try:
                        jsonschema.validate(result, schema)
                    except jsonschema.ValidationError as e:
                        log.warning("%s output failed schema check (%s); keeping it anyway", agent, e.message)
                    return result

            messages.append({"role": "assistant", "content": resp.content})
            if resp.stop_reason == "pause_turn":
                continue  # server-side search/fetch loop paused; resend to let it continue
            if resp.stop_reason == "max_tokens":
                raise AgentError(f"{agent}: hit max_tokens before submitting")
            messages.append({"role": "user", "content": f"Now call {tool_name} with your final result. "
                                                        f"Do not write anything else."})
            force = True

        raise AgentError(f"{agent}: no result after {max_turns} turns")
