#!/usr/bin/python3
for x in range(ord("a"), ord("z") + 1):
    if chr(x) in "qe":
        continue
    print("{}".format(chr(x)), end='')
