#!/usr/bin/python3
"""write_file
"""


def write_file(filename="", text=""):
    """Takes str filename to read, and str text to write to
    """

    with open(filename, mode="w", encoding="utf-8") as writeFile:
        writeFile.write(text)
        return len(text)
