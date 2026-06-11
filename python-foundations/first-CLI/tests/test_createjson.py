from create_json import create_json
import json
def test_create_json_file(tmp_path):

    output_file = tmp_path / "result.json"

    data = {
        "summary": "hello",
        "mode": "brief",
        "input_chars": 5,
    }

    result = create_json(data, output_file)

    assert result == output_file
    assert output_file.exists()

def test_create_json_content(tmp_path):

    output_file = tmp_path / "result.json"

    data = {
        "summary": "hello",
        "mode": "brief",
        "input_chars": 5,
    }

    create_json(data, output_file)

    with output_file.open(
        "r",
        encoding="utf-8"
    ) as f:
        loaded = json.load(f)

    assert loaded == data