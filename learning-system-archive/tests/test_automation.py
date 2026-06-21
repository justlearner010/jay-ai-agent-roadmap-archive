import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

from automation import new_week
from automation.validate_workspace import validate


class NewWeekTests(unittest.TestCase):
    def test_create_week_and_refuse_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            template = root / "templates" / "weekly-plan.md"
            template.parent.mkdir()
            template.write_text("## 验收条件\n", encoding="utf-8")
            config = {
                "paths": {
                    "workspace": "workspace/jay",
                    "weekly_template": "templates/weekly-plan.md",
                }
            }
            with patch.object(new_week, "ROOT", root), patch.object(
                new_week, "load_config", return_value=config
            ):
                output = new_week.create_week(date(2026, 6, 29), "本周主问题")
                self.assertIn("本周主问题", output.read_text(encoding="utf-8"))
                with self.assertRaises(FileExistsError):
                    new_week.create_week(date(2026, 6, 29), "另一个问题")


class ValidationTests(unittest.TestCase):
    def test_repository_is_valid(self):
        self.assertEqual(validate(), [])


if __name__ == "__main__":
    unittest.main()
