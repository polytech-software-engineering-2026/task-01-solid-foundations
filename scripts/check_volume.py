#!/usr/bin/env python3
"""Проверяет, что все 5 кат задания 1 сделаны."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KATAS = ["notifications", "shapes", "discounts", "devices", "payment"]


def main() -> int:
    done = [k for k in KATAS if (ROOT / "katas" / k / "solution.py").exists()]
    missing = [k for k in KATAS if k not in done]

    print(f"Сделано: {len(done)}/{len(KATAS)} — {done}")

    if missing:
        print(f"\nНе хватает: {missing}", file=sys.stderr)
        return 1

    print("Все каты сделаны.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
