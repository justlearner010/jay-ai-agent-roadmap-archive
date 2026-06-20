from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class DailyEntryRequest:
    entry_type: str
    date: str
    template_path: Path
    output_dir: Path
    topic: str | None = None


@dataclass(frozen=True)
class DailyEntry:
    output_path: Path
    content: str


@dataclass(frozen=True)
class CreateResult:
    output_path: Path
    created: bool


def build_entry(request: DailyEntryRequest) -> DailyEntry:
    template = request.template_path.read_text(encoding="utf-8")
    content = template.replace("YYYY-MM-DD", request.date)

    if request.entry_type == "log":
        filename = f"{request.date} 学习日志.md"
    elif request.entry_type == "note":
        filename = f"{request.date} 学习笔记.md"
        topic = request.topic or "填写今天学习的概念"
        content = content.replace("主题：填写今天学习的概念", f"主题：{topic}")
    else:
        raise ValueError(f"Unsupported entry type: {request.entry_type}")

    return DailyEntry(output_path=request.output_dir / filename, content=content)


def create_entry(request: DailyEntryRequest) -> CreateResult:
    entry = build_entry(request)
    entry.output_path.parent.mkdir(parents=True, exist_ok=True)

    if entry.output_path.exists():
        return CreateResult(output_path=entry.output_path, created=False)

    entry.output_path.write_text(entry.content, encoding="utf-8")
    return CreateResult(output_path=entry.output_path, created=True)


def make_request(entry_type: str, entry_date: str, topic: str | None = None) -> DailyEntryRequest:
    if entry_type == "log":
        return DailyEntryRequest(
            entry_type="log",
            date=entry_date,
            template_path=ROOT / "templates" / "daily-learning-log-template.md",
            output_dir=ROOT / "learning-log",
        )
    if entry_type == "note":
        return DailyEntryRequest(
            entry_type="note",
            date=entry_date,
            template_path=ROOT / "templates" / "daily-study-note-template.md",
            output_dir=ROOT / "study-notes",
            topic=topic,
        )
    raise ValueError(f"Unsupported entry type: {entry_type}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="创建当天的学习日志或学习笔记")
    parser.add_argument(
        "entry_type",
        choices=("log", "note"),
        help="log 生成学习日志；note 生成学习笔记",
    )
    parser.add_argument(
        "--date",
        default=date.today().isoformat(),
        help="指定日期，格式为 YYYY-MM-DD；默认使用今天",
    )
    parser.add_argument(
        "--topic",
        default=None,
        help="学习笔记主题，仅 entry_type=note 时使用",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    request = make_request(args.entry_type, args.date, args.topic)
    result = create_entry(request)

    if result.created:
        print(f"已创建：{result.output_path.relative_to(ROOT)}")
    else:
        print(f"已存在，未覆盖：{result.output_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
