#!/usr/bin/python3
from sre_constants import RANGE


for tens in range(0, 10):
    for ones in range(0, 10):
        if ones > tens:
            print("{:d}{:d}".format(tens, ones), end='')
            if tens < 8:
                print(', ', end='')
            else:
                print("")
