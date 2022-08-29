#!/usr/bin/python3
for x in range(ord("a"), ord("z")):
    if chr(x) in "qe":
        continue
    print("{}".format(chr(x)), end='')
