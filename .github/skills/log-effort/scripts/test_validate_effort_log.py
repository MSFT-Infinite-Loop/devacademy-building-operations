import tempfile
import unittest
from datetime import date
from pathlib import Path

from validate_effort_log import summarize, validate

HEADER = "date,participant,work_item,package,activity,hours,evidence\n"


class ValidateEffortLogTests(unittest.TestCase):
    def write_log(self, content: str) -> Path:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "effort-log.csv"
        path.write_text(content, encoding="utf-8")
        return path

    def test_accepts_valid_entry(self) -> None:
        path = self.write_log(
            HEADER
            + "2026-11-15,Carlos Natera,#14,Cross-cutting,code,1.25,"
            + "https://github.com/example/repo/pull/1\n"
        )

        entries, errors = validate(path)

        self.assertEqual([], errors)
        self.assertEqual(1, len(entries))

    def test_rejects_exact_duplicate(self) -> None:
        row = (
            "2026-11-15,Carlos Natera,#14,Cross-cutting,code,1.25,"
            "https://github.com/example/repo/pull/1\n"
        )
        path = self.write_log(HEADER + row + row)

        _, errors = validate(path)

        self.assertTrue(any("exact duplicate" in error for error in errors))

    def test_rejects_invalid_fields(self) -> None:
        path = self.write_log(
            HEADER
            + "15/11/2026,Carlos Natera,14,Cross-cutting,coding,-1,"
            + "missing\n"
        )

        _, errors = validate(path)

        self.assertTrue(any("invalid ISO date" in error for error in errors))
        self.assertTrue(any("work_item must be" in error for error in errors))
        self.assertTrue(any("unsupported activity" in error for error in errors))
        self.assertTrue(any("hours must be" in error for error in errors))

    def test_rejects_wrong_header(self) -> None:
        path = self.write_log("date,participant,hours\n")

        _, errors = validate(path)

        self.assertTrue(any("expected header" in error for error in errors))

    def test_separates_eligible_and_provisional_hours(self) -> None:
        path = self.write_log(
            HEADER
            + "2026-11-11,Carlos Natera,#14,Cross-cutting,design,2,"
            + "https://github.com/example/repo/issues/14\n"
            + "2026-11-15,Carlos Natera,#14,Cross-cutting,code,1.5,"
            + "https://github.com/example/repo/pull/1\n"
        )
        entries, errors = validate(path)

        summary = summarize(entries, date.fromisoformat("2026-11-15"))

        self.assertEqual([], errors)
        self.assertEqual("1.5", summary["eligible_work_items"]["#14"])
        self.assertEqual("2", summary["provisional_work_items"]["#14"])


if __name__ == "__main__":
    unittest.main()
