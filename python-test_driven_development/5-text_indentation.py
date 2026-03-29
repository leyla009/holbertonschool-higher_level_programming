#!/usr/bin/python3
"""This module prints text with 2 new lines after '.', '?' and ':'."""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for ch in text:
        line += ch
        if ch in ".?:":
            print(line.strip(), end="\n\n")
            line = ""

    if line:
        print(line.strip(), end="")
