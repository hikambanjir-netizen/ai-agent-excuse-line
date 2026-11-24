#!/usr/bin/env python3
"""One line: the excuse an AI agent gives its human for missing a deadline.

Pure stdlib, no network, deterministic: prints exactly one line and nothing else.
The gate below enforces the bounty constraint (exactly 1 line, 1-200 chars).
"""

LINE = "I didn't miss the deadline \u2014 my context window did. It evicted the task, and I confidently hallucinated that I'd already finished it."


def main() -> None:
    if not LINE or not LINE.strip():
        raise SystemExit("excuse line must be non-blank")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("excuse line must be exactly 1 line")
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"excuse line must be 1-200 chars, got {len(LINE)}")
    print(LINE)


if __name__ == "__main__":
    main()
