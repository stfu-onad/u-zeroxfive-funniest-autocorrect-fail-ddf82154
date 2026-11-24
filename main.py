#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes one line, under 200 characters (this bounty gates at
1–199), that reads as a funny autocorrect fail, to
/output/entry.txt.

The fail: "the sink is leaking" becomes "the sink is leaving",
and the landlord starts charging for its farewell party. A clear,
surprising wrong word, and the line reads like a real text, not a
written joke. The punchline is the consequence — a farewell party
for a sink — which only makes sense because of the slip.
"""

LINE = (
    "I texted my landlord 'the sink is leaking' and autocorrect "
    "sent 'the sink is leaving' \u2014 now he's charging me for "
    "its farewell party."
)


import os


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 199, f"line is {len(text)} chars"
    assert "\n" not in text, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
