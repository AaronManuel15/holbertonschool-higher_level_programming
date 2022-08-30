#!/usr/bin/python3
def uppercase(str):
    newString = ''
    for x in str:
        if ord(x) in range(97, 123):
            x = ord(x) - 32
            newString = newString + chr(x)
        else:
            newString = newString + x
    print("{}".format(newString))
