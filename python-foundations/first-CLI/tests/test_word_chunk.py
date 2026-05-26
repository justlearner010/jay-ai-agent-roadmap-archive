import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from word_chunk import text_chunk


def test_text_chunk_basic(tmp_path):
    test_file = tmp_path / "sample].txt"
    test_file.write_text("abcdef", encoding="utf-8")

    result = text_chunk(test_file, 2)

    assert result == [
        {
            "chunk index": 1,
            "chunk_start": 0,
            "chunk_end": 2,
            "chunk_text": "ab",
        },
        {
            "chunk index": 2,
            "chunk_start": 2,
            "chunk_end": 4,
            "chunk_text": "cd",
        },
        {
            "chunk index": 3,
            "chunk_start": 4,
            "chunk_end": 6,
            "chunk_text": "ef",
        },
    ]