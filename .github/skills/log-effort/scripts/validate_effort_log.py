#!/usr/bin/env python3

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path

EXPECTED_FIELDS = [
    "date",
    "participant",
    "work_item",
    "package",
    "activity",
    "hours",
    "evidence",
]
ACTIVITIES = {
    "design",
    "code",
    "test",
    "review",
    "docs",
    "ops",
    "meeting",
    "learning",
}
WORK_ITEM = re.compile(r"#[1-9][0-9]*$")


def validate(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    entries: list[dict[str, str]] = []
    errors: list[str] = []
    seen: dict[tuple[str, ...], int] = {}

    try:
        handle = path.open(newline="", encoding="utf-8-sig")
    except OSError as error:
        return entries, [f"{path}: {error}"]

    with handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != EXPECTED_FIELDS:
            return entries, [
                f"{path}: expected header {','.join(EXPECTED_FIELDS)}; "
                f"found {','.join(reader.fieldnames or [])}"
            ]

        for line_number, raw in enumerate(reader, start=2):
            if None in raw:
                errors.append(f"line {line_number}: unexpected extra columns")
                continue

            row = {field: (raw.get(field) or "").strip() for field in EXPECTED_FIELDS}
            missing = [field for field, value in row.items() if not value]
            if missing:
                errors.append(
                    f"line {line_number}: missing required fields {', '.join(missing)}"
                )
                continue

            try:
                date.fromisoformat(row["date"])
            except ValueError:
                errors.append(
                    f"line {line_number}: invalid ISO date '{row['date']}'"
                )

            if not WORK_ITEM.fullmatch(row["work_item"]):
                errors.append(
                    f"line {line_number}: work_item must be #<number>, "
                    f"found '{row['work_item']}'"
                )

            if row["activity"] not in ACTIVITIES:
                errors.append(
                    f"line {line_number}: unsupported activity '{row['activity']}'"
                )

            try:
                hours = Decimal(row["hours"])
                if not hours.is_finite() or hours <= 0:
                    raise ValueError
            except (InvalidOperation, ValueError):
                errors.append(
                    f"line {line_number}: hours must be a positive decimal"
                )

            key = tuple(row[field] for field in EXPECTED_FIELDS)
            if key in seen:
                errors.append(
                    f"line {line_number}: exact duplicate of line {seen[key]}"
                )
            else:
                seen[key] = line_number

            entries.append(row)

    return entries, errors


def summarize(
    entries: list[dict[str, str]], eligible_from: date | None = None
) -> dict[str, object]:
    totals: defaultdict[str, Decimal] = defaultdict(Decimal)
    participants: defaultdict[str, Decimal] = defaultdict(Decimal)
    eligible_totals: defaultdict[str, Decimal] = defaultdict(Decimal)
    provisional_totals: defaultdict[str, Decimal] = defaultdict(Decimal)

    for row in entries:
        try:
            hours = Decimal(row["hours"])
        except InvalidOperation:
            continue
        totals[row["work_item"]] += hours
        participants[row["participant"]] += hours
        if eligible_from is not None:
            try:
                work_date = date.fromisoformat(row["date"])
            except ValueError:
                continue
            destination = (
                eligible_totals if work_date >= eligible_from else provisional_totals
            )
            destination[row["work_item"]] += hours

    total_hours = sum(totals.values(), Decimal())
    summary: dict[str, object] = {
        "entries": len(entries),
        "total_hours": str(total_hours),
        "work_items": {key: str(totals[key]) for key in sorted(totals)},
        "participants": {
            key: str(participants[key]) for key in sorted(participants)
        },
    }
    if eligible_from is not None:
        summary.update(
            {
                "eligible_from": eligible_from.isoformat(),
                "eligible_total_hours": str(
                    sum(eligible_totals.values(), Decimal())
                ),
                "eligible_work_items": {
                    key: str(eligible_totals[key]) for key in sorted(eligible_totals)
                },
                "provisional_total_hours": str(
                    sum(provisional_totals.values(), Decimal())
                ),
                "provisional_work_items": {
                    key: str(provisional_totals[key])
                    for key in sorted(provisional_totals)
                },
            }
        )
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the capstone effort log.")
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=Path("docs/team/effort-log.csv"),
    )
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument(
        "--eligible-from",
        type=date.fromisoformat,
        help="Report rows before this ISO date as provisional.",
    )
    args = parser.parse_args()

    entries, errors = validate(args.path)
    summary = summarize(entries, args.eligible_from)

    if args.as_json:
        print(json.dumps({"valid": not errors, "errors": errors, **summary}, indent=2))
    else:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        if not errors:
            print(
                f"Valid effort log: {summary['entries']} entries, "
                f"{summary['total_hours']} total hours."
            )
            for item, hours in summary["work_items"].items():
                print(f"  {item}: {hours}")
            if args.eligible_from is not None:
                print(
                    f"Eligible from {args.eligible_from}: "
                    f"{summary['eligible_total_hours']} hours; "
                    f"provisional: {summary['provisional_total_hours']} hours."
                )

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
