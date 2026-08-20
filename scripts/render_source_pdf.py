#!/usr/bin/env python3
"""Render a PDF to numbered PNG pages without reading its text layer."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--dpi", type=int, default=200)
    parser.add_argument("--first", type=int)
    parser.add_argument("--last", type=int)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    source = args.source.resolve()
    output_dir = args.output_dir.resolve()
    if not source.is_file():
        parser.error(f"source PDF not found: {source}")
    if args.dpi <= 0:
        parser.error("--dpi must be positive")
    if args.first is not None and args.first <= 0:
        parser.error("--first must be positive")
    if args.last is not None and args.last <= 0:
        parser.error("--last must be positive")
    if args.first and args.last and args.first > args.last:
        parser.error("--first cannot exceed --last")

    renderer = shutil.which("pdftoppm")
    if renderer is None:
        parser.error("pdftoppm was not found on PATH")

    output_dir.mkdir(parents=True, exist_ok=True)
    existing = list(output_dir.glob("page-*.png"))
    if existing and not args.force:
        parser.error(
            f"{output_dir} already contains page PNGs; use --force to replace them"
        )
    if args.force:
        for path in existing:
            path.unlink()

    raw_prefix = output_dir / "rendered"
    command = [renderer, "-png", "-r", str(args.dpi)]
    if args.first is not None:
        command.extend(["-f", str(args.first)])
    if args.last is not None:
        command.extend(["-l", str(args.last)])
    command.extend([str(source), str(raw_prefix)])
    subprocess.run(command, check=True)

    rendered = []
    for path in output_dir.glob("rendered-*.png"):
        match = re.fullmatch(r"rendered-(\d+)", path.stem)
        if match:
            rendered.append((int(match.group(1)), path))
    if not rendered:
        raise RuntimeError("pdftoppm produced no page PNGs")

    for page, path in sorted(rendered):
        target = output_dir / f"page-{page:04d}.png"
        path.replace(target)

    print(f"Rendered {len(rendered)} page(s) at {args.dpi} dpi into {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
