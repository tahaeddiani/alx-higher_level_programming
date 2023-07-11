#!/usr/bin/python3
"""write to file"""


def write_file(filename="", text=""):
    """write file func"""
    with open(filename, 'w', encoding="utf-8") as wf:
        wf.write(text)
        return len(text)
