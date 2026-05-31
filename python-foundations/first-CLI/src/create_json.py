import json
import sys
def create_json(chunks):
    try:
        with open("test.json","w")as f:
            json.dump(
                chunks,
                f,
                ensure_ascii=False,
                indent=4
            )
    except FileNotFoundError:
        sys.exit("File does not exist")