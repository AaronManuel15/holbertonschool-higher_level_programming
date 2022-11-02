#!/usr/bin/python3
""" Task 0
"""

if __name__ == "__main__":
    import requests
    resp = requests.get("https://intranet.hbtn.io/status")
    print("""Body response:
\t- type: {}
\t- content: {}""".format(type(resp.text), resp.text))
