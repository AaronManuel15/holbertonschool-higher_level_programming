#!/usr/bin/python3
""" Task 6
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    print(requests.post(argv[1], data={'email': argv[2]}).text)
