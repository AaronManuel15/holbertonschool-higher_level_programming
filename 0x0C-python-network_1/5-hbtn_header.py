#!/usr/bin/python3
""" Task 5
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    resp = requests.get(argv[1])
    print(resp.headers.get("X-Request-Id"))
