from text_status import TextStats



def test_all(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text(
        "hello world\n"
        "python 123\n"
        "456"
    )

    stats = TextStats(file)

    assert stats.line_check() == 3
    assert stats.word_check() == 5
    assert stats.digit_check() == 6
    assert stats.space_check() == 4