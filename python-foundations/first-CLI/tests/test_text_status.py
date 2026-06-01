import pytest
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
    
def test_empty_file(tmp_path):
    file = tmp_path / "empty.txt"
    file.write_text("")

    stats = TextStats(str(file))

    assert stats.line_check() == 0
    assert stats.word_check() == 0
    assert stats.space_check() == 0
    assert stats.digit_check() == 0


def test_file_not_found():
    stats = TextStats("not_exist.txt")

    with pytest.raises(FileNotFoundError):
        stats.word_check()