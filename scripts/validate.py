#!/usr/bin/env python3
from pathlib import Path
import datetime
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = {"roomcord": "Roomcord", "autoworker-hub": "Autoworker Hub", "hermes-hub": "Hermes Hub"}
REQUIRED = ("product", "product_name", "title", "date", "version", "summary")
FORBIDDEN = re.compile(r"(?:github\.com/(?:fulldiveVR|jetcalls)/[^/\s]+/(?:commit|pull|issues)|\b[0-9a-f]{40}\b|sk-[A-Za-z0-9_-]{16,})", re.I)


def front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("missing YAML front matter")
    block = text.split("\n---\n", 1)[0][4:]
    values = {}
    for line in block.splitlines():
        if line and not line.startswith((" ", "-")) and ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"')
    if FORBIDDEN.search(text):
        raise ValueError("contains a private link, commit hash, or secret-like value")
    return values


errors = []
seen = set()
for path in sorted((ROOT / "_releases").glob("*/*.md")):
    try:
        data = front_matter(path)
        missing = [key for key in REQUIRED if not data.get(key)]
        if missing:
            raise ValueError(f"missing fields: {', '.join(missing)}")
        product = data["product"]
        if product not in PRODUCTS or data["product_name"] != PRODUCTS[product]:
            raise ValueError("unknown product or mismatched product_name")
        datetime.date.fromisoformat(data["date"])
        if path.parent.name != product or not path.name.startswith(data["date"] + "-"):
            raise ValueError("path must match product and date")
        identity = (product, data["version"])
        if identity in seen:
            raise ValueError("duplicate product/version")
        seen.add(identity)
    except ValueError as error:
        errors.append(f"{path.relative_to(ROOT)}: {error}")

if not seen:
    errors.append("no release notes found")
if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)
print(f"Validated {len(seen)} release notes")

