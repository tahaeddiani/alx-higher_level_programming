#!/usr/bin/python3
def lastofdig(number):
    sign = '-'
    lastofdigit = abs(number) % 10
    if number < 0 :
        return sign + str(lastofdigit)
    else:
        return lastofdigit
