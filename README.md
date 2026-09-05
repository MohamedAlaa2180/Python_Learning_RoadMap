# Python Learning

Phase 0 of an AI Engineer path. Current ship: a CLI that summarizes a folder of `.txt` and `.json` files.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## File summarizer (P0-04)

From the project root:

```powershell
python src/summarize.py data/samples
```

That prints counts (files, JSON keys, text lines) and writes `data/samples/summary.json`.

```powershell
python src/summarize.py --help
python src/summarize.py some\other\folder -o summary.json
```

Missing folders print an error and exit with code 1. `summary.json` inside the target folder is skipped so re-runs do not count the output file.
