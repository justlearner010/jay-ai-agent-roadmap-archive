from pathlib import Path
import tomllib


ROOT = Path(__file__).resolve().parents[1]


def load_config() -> dict:
    with (ROOT / "learning-system.toml").open("rb") as file:
        return tomllib.load(file)
