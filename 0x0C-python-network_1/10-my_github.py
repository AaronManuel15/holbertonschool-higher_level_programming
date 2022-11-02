#!/usr/bin/python3
""" Task 9
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    req = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))
    js = req.json()
    print(js.get('id'))
