from pathlib import Path
import json
import logging
import sys
output_path = Path("output") / "chunks.json"

logger = logging.getLogger(__name__)
def create_json(chunks):
    try:
        with output_path.open("w",encoding="utf-8")as f:
            json.dump(
                chunks,
                f,
                ensure_ascii=False,
                indent=4
            )
    except FileNotFoundError:
        logger.exception("文件读取失败")
        raise