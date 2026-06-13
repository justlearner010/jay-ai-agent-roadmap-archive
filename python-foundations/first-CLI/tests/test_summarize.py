# import pytest

# from summarize import summarize_text


# def test_summarize_brief_counts_words():
#     result = summarize_text("hello world", mode="brief")

#     assert result == "Brief summary: this text has 2 words"


# def test_summarize_empty_text():
#     result = summarize_text("", mode="brief")

#     assert result == "No content to summarize."


# def test_summarize_bullets_counts_words_and_characters():
#     result = summarize_text("hello world", mode="bullets")

#     assert result == [
#         "- Word count: 2",
#         "- Character count: 11",
#         "- Mock summary: this is a placeholder summary.",
#     ]


# def test_summarize_rejects_unknown_mode():
#     with pytest.raises(ValueError):
#         summarize_text("hello world", mode="unknown")


import pytest

from summarize import summarize_text


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