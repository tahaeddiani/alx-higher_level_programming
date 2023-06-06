#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
cnv_str = str(number)
short_it = cnv_str[-1]
if number > 0 or number == 0:
    if int(short_it) > 5:
        print(f"Last digit of {number} is {short_it} and is greater than 5")
    elif int(short_it) == 0:
        print(f"Last digit of {number} is {short_it} and is 0")
    elif int(short_it) < 6 and int(short_list) != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, short_it)
else:
    print(f"Last digit of {number} is -{short_it} and is less than 6"
    " and not 0")
