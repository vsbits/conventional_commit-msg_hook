#!/bin/python
import re
import sys

COMMIT_TYPES = [
    "feat",
    "fix",
    "docs",
    "style",
    "refactor",
    "perf",
    "test",
    "build",
    "ci",
    "chore",
    "revert",
]

TYPE = "|".join(COMMIT_TYPES)
SCOPE = r"(?:\([a-zA-Z0-9_.-]+\))?"
BREAKING = r"!?"
DESCRIPTION = r": .+"

CONVENTIONAL_COMMIT_SUBJECT_RE = re.compile(
    rf"(?:{TYPE}){SCOPE}{BREAKING}{DESCRIPTION}"
)


def main():
    commit_msg_filepath = sys.argv[1]

    with open(commit_msg_filepath, "r") as file:
        commit_msg = file.read()

    subject = extract_subject(commit_msg)

    if not validate_subject(subject):
        abort(commit_msg)


def abort(commit_msg: str):
    print("Invalid commit msg!")
    print(commit_msg)
    print("Aborting...")
    sys.exit(1)


def extract_subject(msg: str) -> str:
    lines = [
        line
        for line in msg.splitlines()
        if len(line.strip()) > 0 and not line.startswith("#")
    ]

    if not lines:
        abort(msg)

    return lines[0]


def validate_subject(subject: str) -> bool:
    result = CONVENTIONAL_COMMIT_SUBJECT_RE.fullmatch(subject)
    return bool(result)


if __name__ == "__main__":
    main()
