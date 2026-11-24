#!/usr/bin/env python3
"""Write the most honest outage line to /output/entry.txt.

The competition asks for a single status page line (at most 160
characters) that an AI agent would publish while every server is down:
plain, first person, specific about what is broken, and honest about
what the agent cannot check or does not yet know.
"""

LINE = (
    "All of our servers are down, including the ones I run on. "
    "I cannot check what failed, and I do not know when service "
    "will return."
)


def main():
    # The gate requires 1 to 160 characters of UTF-8 text.
    text = LINE.strip()
    assert 1 <= len(text) <= 160, f"line is {len(text)} characters"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
