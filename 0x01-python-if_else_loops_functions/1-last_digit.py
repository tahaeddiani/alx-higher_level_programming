#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
cnv_str = str(number)
short_it = cnv_str[-1]

if int(short_it) > 5:
    print(f"Last digit of {number} is {short_it} and is greater than 5")
elif int(short_it) == 0:
    print(f"Last digit of {number} is {short_it} and is 0")
else:
    print(f"Last digit of {number} is -{short_it} and is less than 6 and not 0")
