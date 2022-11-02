#!/usr/bin/python3
""" Task 3
"""

if __name__ == "__main__":
    from urllib import request, parse, error
    from sys import argv

    try:
        with request.urlopen(argv[1]) as resp:
            resp = resp.read().decode('utf8')
            print(resp)

    except error.HTTPError as uhoh:
        print("Error code: {}".format(uhoh.code))
