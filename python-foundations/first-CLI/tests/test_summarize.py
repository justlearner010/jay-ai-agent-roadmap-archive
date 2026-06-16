import pytest
from openai import OpenAI
from summarize import (
    summarize_text,
    MOCKLLM,
    Summarizer,
    OpenAILLM
)


@pytest.mark.parametrize(
    "text,expected",
    [
        (
            "hello world",
            "Brief summary: this text has 2 words",
        ),
        (
            "你好 世界",
            "Brief summary: this text has 2 words",
        ),
        (
            "",
            "No content to summarize.",
        ),
    ],
)
def test_summarize_brief(text, expected):

    assert summarize_text(text, mode="brief") == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        (
            "hello world",
            [
                "- Word count: 2",
                "- Character count: 11",
                "- Mock summary: this is a placeholder summary.",
            ],
        ),
        (
            "你好 世界",
            [
                "- Word count: 2",
                "- Character count: 5",
                "- Mock summary: this is a placeholder summary.",
            ],
        ),
    ],
)
def test_summarize_bullets(text, expected):
    assert summarize_text(text, mode="bullets") == expected


@pytest.mark.parametrize(
    "mode",
    [
        "unknown",
        "abc",
        "detail",
        "summary",
        "123",
    ],
)
def test_summarize_rejects_unknown_mode(mode):
    with pytest.raises(ValueError):
        summarize_text("hello world", mode=mode)


@pytest.mark.xfail(
    reason="Chinese segmentation is not implemented yet"
)
@pytest.mark.parametrize(
    "text,expected",
    [
        (
            "你好世界",
            "Brief summary: this text has 2 words",
        ),
    ],
)
def test_future_chinese_word_segmentation(text, expected):
    assert summarize_text(text, mode="brief") == expected


def test_mock_llm():
    llm = MOCKLLM()

    result = llm.summarize("hello")

    assert result == "fake summary"

def test_openai_llm(monkeypatch):

    class FakeResponse:
        output_text = "fake gpt answer"

    def fake_create(*args,**kwargs):
        return FakeResponse()
    
    monkeypatch.setattr(
        "openai.resources.responses.Responses.create",
        fake_create
    )

    llm = OpenAILLM()

    result = llm.summarize_with_llm("hello")

    assert result == "fake gpt answer"