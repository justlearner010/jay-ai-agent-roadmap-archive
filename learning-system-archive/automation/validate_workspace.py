import csv
import re
from pathlib import Path
from urllib.parse import unquote

from .config import ROOT, load_config


REQUIRED_COLUMNS = {
    "周开始",
    "周结束",
    "本周主问题",
    "探索小时",
    "周中诊断",
    "验收状态",
    "下周决策",
}
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def _without_code_fences(text: str) -> str:
    parts = text.split("```")
    return "".join(parts[::2])


def find_broken_links() -> list[str]:
    problems: list[str] = []
    for document in ROOT.rglob("*.md"):
        if ".git" in document.parts:
            continue
        text = _without_code_fences(document.read_text(encoding="utf-8"))
        for raw_target in LINK_PATTERN.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or "://" in target or target.startswith(("mailto:", "#")):
                continue
            resolved = (document.parent / unquote(target)).resolve()
            if not resolved.exists():
                problems.append(f"{document.relative_to(ROOT)} -> {raw_target}")
    return problems


def validate() -> list[str]:
    config = load_config()
    problems: list[str] = []
    for required in ("framework", "task-library", "templates", "automation", "tests"):
        if not (ROOT / required).is_dir():
            problems.append(f"missing directory: {required}")

    workspace = ROOT / config["paths"]["workspace"]
    if not workspace.is_dir():
        problems.append(f"missing workspace: {workspace.relative_to(ROOT)}")

    weekly_log = ROOT / config["paths"]["weekly_log"]
    if not weekly_log.is_file():
        problems.append(f"missing weekly log: {weekly_log.relative_to(ROOT)}")
    else:
        with weekly_log.open(encoding="utf-8", newline="") as file:
            columns = set(next(csv.reader(file), []))
        missing = REQUIRED_COLUMNS - columns
        if missing:
            problems.append(f"weekly log missing columns: {', '.join(sorted(missing))}")

    problems.extend(find_broken_links())
    return problems


def main() -> None:
    problems = validate()
    if problems:
        print("Workspace validation failed:")
        for problem in problems:
            print(f"- {problem}")
        raise SystemExit(1)
    print("Workspace validation passed.")


if __name__ == "__main__":
    main()
