"""CLI: summarize a folder of .txt / .json files into summary.json."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path

COUNTED_EXTS = {".txt", ".json"}
OUTPUT_NAME = "summary.json"


@dataclass
class FileStat:
    name: str
    ext: str
    lines: int | None = None
    keys: int | None = None
    error: str | None = None


def count_json_keys(data: object) -> int:
    """Top-level keys for a dict, length for a list."""
    if isinstance(data, dict):
        return len(data)
    if isinstance(data, list):
        return len(data)
    return 0


def summarize_file(path: Path) -> FileStat:
    ext = path.suffix.lower()
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return FileStat(name=path.name, ext=ext, error=str(exc))

    if ext == ".txt":
        return FileStat(name=path.name, ext=ext, lines=len(text.splitlines()))

    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        return FileStat(name=path.name, ext=ext, error=f"invalid JSON: {exc.msg}")

    return FileStat(name=path.name, ext=ext, keys=count_json_keys(data))


def list_input_files(folder: Path) -> list[Path]:
    files = [
        path
        for path in folder.iterdir()
        if path.is_file()
        and path.suffix.lower() in COUNTED_EXTS
        and path.name != OUTPUT_NAME
    ]
    return sorted(files, key=lambda path: path.name.lower())


def summarize_folder(folder: Path) -> dict:
    stats = [summarize_file(path) for path in list_input_files(folder)]
    by_ext = Counter(stat.ext for stat in stats)
    total_lines = sum(stat.lines or 0 for stat in stats)
    total_keys = sum(stat.keys or 0 for stat in stats)

    return {
        "folder": folder.as_posix(),
        "files": len(stats),
        "by_ext": dict(sorted(by_ext.items())),
        "total_lines": total_lines,
        "total_json_keys": total_keys,
        "files_detail": [
            {key: value for key, value in asdict(stat).items() if value is not None}
            for stat in stats
        ],
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Count .txt lines and .json keys in a folder, then write summary.json."
    )
    parser.add_argument(
        "folder",
        type=Path,
        help="Folder that contains .txt and/or .json files",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help=f"Output path (default: <folder>/{OUTPUT_NAME})",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    folder = args.folder

    if not folder.exists():
        print(f"Folder not found: {folder}", file=sys.stderr)
        return 1
    if not folder.is_dir():
        print(f"Not a folder: {folder}", file=sys.stderr)
        return 1

    summary = summarize_folder(folder)
    output = args.output or (folder / OUTPUT_NAME)
    output.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    print(
        f"{summary['files']} files, "
        f"{summary['total_json_keys']} json keys, "
        f"{summary['total_lines']} lines"
    )
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
