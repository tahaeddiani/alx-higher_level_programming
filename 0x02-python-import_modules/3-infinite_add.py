#!/usr/bin/env python3
import sys
if __name__ == "__main__":
    x = sys.argv[1:]
    y = 0
    for i in x:
        y += int(i)
    print(y)
