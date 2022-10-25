#!/usr/bin/python3
"""read_lines
"""
import os


def read_lines(filename="", nb_lines=0):
    """Takes in str filename to read, and n lines w/ int nb_lines
    """


    with open(filename, encoding="utf-8") as readFile:
        lineNum = 0
        while True:
            line = readFile.readline()
            lineNum += 1
            print(line, end='')
            if lineNum >= nb_lines and nb_lines > 0:
                break 
            if not line:
                break
