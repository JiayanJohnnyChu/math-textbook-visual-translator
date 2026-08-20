#!/usr/bin/env python3
"""Check SOURCE_PDF_PAGE markers across LaTeX source files."""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path


MARKER = re.compile(r"^\s*%\s*SOURCE_PDF_PAGE:\s*(\d+)\s*$")


def collect_tex_files(paths: list[Path]) -> list[Path]:
    files: set[Path] = set()
    for raw_path in paths:
        path = raw_path.resolve()
        if path.is_file() and path.suffix.lower() == ".tex":
            files.add(path)
        elif path.is_dir():
            files.update(item for item in path.rglob("*.tex") if item.is_file())
        else:
            raise FileNotFoundError(f"not a TeX file or directory: {path}")
    return sorted(files)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--first", type=int, required=True)
    parser.add_argument("--last", type=int, required=True)
    args = parser.parse_args()
    if args.first <= 0 or args.last < args.first:
        parser.error("expected 0 < --first <= --last")

    locations: dict[int, list[str]] = defaultdict(list)
    files = collect_tex_files(args.paths)
    for path in files:
        for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            match = MARKER.match(line)
            if match:
                locations[int(match.group(1))].append(f"{path}:{line_number}")

    expected = set(range(args.first, args.last + 1))
    actual = set(locations)
    missing = sorted(expected - actual)
    outside = sorted(actual - expected)
    duplicates = {page: refs for page, refs in locations.items() if len(refs) > 1}

    print(f"TeX files scanned: {len(files)}")
    print(f"Expected source pages: {args.first}-{args.last} ({len(expected)})")
    print(f"Unique markers found: {len(actual)}")
    if missing:
        print("Missing pages: " + ", ".join(map(str, missing)))
    if outside:
        print("Out-of-range pages: " + ", ".join(map(str, outside)))
    if duplicates:
        print("Duplicate page markers:")
        for page in sorted(duplicates):
            print(f"  {page}: " + "; ".join(duplicates[page]))

    if missing or outside or duplicates:
        return 1
    print("Coverage check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
