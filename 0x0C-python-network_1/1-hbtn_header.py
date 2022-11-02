#!/usr/bin/python3
""" Task 1
"""

if __name__ == "__main__":
    from urllib import request
    from sys import argv
    with request.urlopen(argv[1]) as resp:
        resp = resp.info()
        print(resp.get("X-Request-Id"))
