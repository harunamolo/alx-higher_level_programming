#!/usr/bin/python3
"""number_of_lines
"""


def number_of_lines(filename=""):
    """Takes in str filename to read the number of lines
    """

    with open(filename, encoding="utf-8") as readFile:
        lines = 0
        while True:
            line = readFile.readline()
            if not line:
                break
            lines += 1
        return lines
