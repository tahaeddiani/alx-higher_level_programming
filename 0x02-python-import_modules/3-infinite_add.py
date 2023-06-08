#!/usr/bin/python3
import sys
if __name__ == '__main__':
    ty = 0
    i = 1
    x = sys.argv
    y = len(x) - 1
    while i != len(x):
        ty = ty + int(x[i])
        i += 1
    print(ty)
