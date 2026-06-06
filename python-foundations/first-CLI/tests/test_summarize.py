import pytest

from summarize import summarize_text


def test_summarize_brief_counts_words():
    result = summarize_text("hello world", mode="brief")

    assert result == "Brief summary: this text has 2 words"


def test_summarize_bullets_counts_words_and_characters():
    result = summarize_text("hello world", mode="bullets")

    assert result == [
        "- Word count: 2",
        "- Character count: 11",
        "- Mock summary: this is a placeholder summary.",
    ]


def test_summarize_rejects_unknown_mode():
    with pytest.raises(ValueError):
        summarize_text("hello world", mode="unknown")
