#!/usr/bin/python3
""" Task 8
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    if argv[1]:
        data = {"q": argv[1]}
    else:
        data = {"q": ""}
    req = requests.post("http://0.0.0.0:5000/search_user", data)
    try:
        js = req.json()
        if js.get('id') is None:
            print("No result")
        else:
            print("[{}] {}".format(js.get('id'), js.get('name')))
    except Exception:
        print("Not a valid JSON")
