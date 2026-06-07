#!/usr/bin/env python3
"""Public-side doc-parity gate.

The public repo has no source code, so it cannot introspect the app. Instead it
vendors `feature-manifest.json` (the code-derived feature surface, synced from
the private repo) and verifies that every `fialr <command>` referenced in the
docs, README, and CHANGELOG is a REAL command. This catches drift and typos
(e.g. documenting a renamed or non-existent command) without the source.

Usage:
    python scripts/check_docs_parity.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "feature-manifest.json"

# Words that can follow "fialr" in prose without being a subcommand.
_NON_COMMANDS = {"is", "the", "a", "can", "will", "to", "and", "or", "uses"}

# Files to scan.
_SCAN = ["README.md", "CHANGELOG.md"]
_SCAN_GLOBS = ["docs/**/*.md"]


def _commands() -> set[str]:
    if not MANIFEST.exists():
        print("feature-manifest.json missing -- sync it from the private repo.")
        sys.exit(1)
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    return set(data.get("commands", []))


def _docs() -> list[Path]:
    files = [ROOT / f for f in _SCAN if (ROOT / f).exists()]
    for pattern in _SCAN_GLOBS:
        files.extend(sorted(ROOT.glob(pattern)))
    return files


def _code_spans(text: str) -> str:
    """Return only fenced + inline code from a markdown document.

    Real command invocations are always in code formatting; scanning prose
    would false-positive on phrases like "each fialr release".
    """
    spans = re.findall(r"```.*?```", text, re.DOTALL)
    spans += re.findall(r"`[^`\n]+`", text)
    return "\n".join(spans)


def main() -> int:
    commands = _commands()
    # Match `fialr <word>` where word is a lowercase token (a candidate command).
    pat = re.compile(r"\bfialr\s+([a-z][a-z-]{1,})\b")
    errors: list[str] = []
    for doc in _docs():
        text = _code_spans(doc.read_text(encoding="utf-8"))
        rel = doc.relative_to(ROOT)
        for m in pat.finditer(text):
            cmd = m.group(1)
            if cmd in _NON_COMMANDS or cmd in commands:
                continue
            errors.append(f"  {rel}: 'fialr {cmd}' is not a known command")

    if errors:
        print("Doc-parity FAILED -- docs reference unknown commands:")
        print("\n".join(sorted(set(errors))))
        print(f"\nKnown commands: {', '.join(sorted(commands))}")
        return 1
    print(f"Doc-parity OK -- all command references valid ({len(commands)} commands).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
