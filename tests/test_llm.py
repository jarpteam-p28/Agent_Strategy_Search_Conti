"""Tests the agent loop in ClaudeLLM against a fake Anthropic client."""
from types import SimpleNamespace as NS

import pytest

from conti_agents.llm import AgentError, ClaudeLLM, web_search_tool

SCHEMA = {"type": "object", "properties": {"x": {"type": "integer"}}, "required": ["x"]}
USAGE = NS(input_tokens=10, output_tokens=5, cache_read_input_tokens=0, cache_creation_input_tokens=0)


def msg(stop, *blocks):
    return NS(stop_reason=stop, content=list(blocks), usage=USAGE)


class FakeClient:
    def __init__(self, replies):
        self.replies = list(replies)
        self.requests = []
        self.messages = self

    def stream(self, **kwargs):
        self.requests.append(kwargs)
        reply = self.replies.pop(0)

        class S:
            def __enter__(s): return s
            def __exit__(s, *a): return False
            def get_final_message(s): return reply
        return S()


def call(client, server_tools=None):
    return ClaudeLLM(client).structured(agent="t", model="m", system="sys", content="hi",
                                        tool_name="submit", schema=SCHEMA, server_tools=server_tools)


def test_forced_tool_without_server_tools():
    c = FakeClient([msg("tool_use", NS(type="tool_use", name="submit", input={"x": 1}))])
    assert call(c) == {"x": 1}
    assert c.requests[0]["tool_choice"] == {"type": "tool", "name": "submit"}


def test_pause_turn_then_nudge_then_submit():
    c = FakeClient([
        msg("pause_turn", NS(type="server_tool_use", name="web_search")),
        msg("end_turn", NS(type="text", text="here is what I found")),
        msg("tool_use", NS(type="tool_use", name="submit", input={"x": 2})),
    ])
    assert call(c, [web_search_tool(3)]) == {"x": 2}
    assert "tool_choice" not in c.requests[0]
    assert "tool_choice" not in c.requests[1]          # pause_turn just resumes
    assert c.requests[2]["tool_choice"]["name"] == "submit"  # nudged + forced
    assert c.requests[2]["messages"][-1]["content"].startswith("Now call submit")


def test_max_tokens_raises():
    c = FakeClient([msg("max_tokens", NS(type="text", text="..."))])
    with pytest.raises(AgentError):
        call(c, [web_search_tool(3)])


class RejectsForcedClient(FakeClient):
    """Mimics the real API error: 'tool_choice: type "tool" and "any" are not supported for this model.'"""
    def stream(self, **kwargs):
        if "tool_choice" in kwargs:
            self.requests.append(kwargs)
            raise RuntimeError('Error code: 400 - tool_choice: type "tool" and "any" are not supported for this model.')
        return super().stream(**kwargs)


def test_falls_back_when_forced_tool_choice_rejected():
    c = RejectsForcedClient([
        msg("end_turn", NS(type="text", text="thinking out loud")),
        msg("tool_use", NS(type="tool_use", name="submit", input={"x": 3})),
    ])
    llm = ClaudeLLM(c)
    out = llm.structured(agent="t", model="opus", system="s", content="hi", tool_name="submit", schema=SCHEMA)
    assert out == {"x": 3}
    assert "opus" in llm.no_forced_tool
    sent = [r for r in c.requests if "tool_choice" not in r]
    assert len(sent) == 2 and sent[1]["messages"][-1]["content"].startswith("Now call submit")
