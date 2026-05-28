import json
def create_json(chunks):
    with open("test.json","w")as f:
        json.dump(
            chunks,
            f,
            ensure_ascii=False,
            indent=4
        )