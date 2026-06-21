import argparse
from datetime import date
from pathlib import Path

from .config import ROOT, load_config


def create_week(start: date, question: str) -> Path:
    config = load_config()
    workspace = ROOT / config["paths"]["workspace"]
    weeks = workspace / "weeks"
    weeks.mkdir(parents=True, exist_ok=True)
    year, week, _ = start.isocalendar()
    destination = weeks / f"{year}-W{week:02d}.md"
    if destination.exists():
        raise FileExistsError(f"Refusing to overwrite {destination.relative_to(ROOT)}")

    template_path = ROOT / config["paths"]["weekly_template"]
    template = template_path.read_text(encoding="utf-8")
    header = (
        f"# {year}-W{week:02d}\n\n"
        f"- 开始日期：{start.isoformat()}\n"
        f"- 本周主问题：{question}\n\n"
    )
    destination.write_text(header + template, encoding="utf-8")
    return destination


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a weekly learning plan.")
    parser.add_argument("--start", required=True, type=date.fromisoformat)
    parser.add_argument("--question", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        destination = create_week(args.start, args.question)
    except FileExistsError as error:
        raise SystemExit(str(error)) from error
    print(destination.relative_to(ROOT))


if __name__ == "__main__":
    main()
