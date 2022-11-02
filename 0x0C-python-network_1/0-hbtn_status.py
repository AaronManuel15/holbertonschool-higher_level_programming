#!/usr/bin/python3
""" Task 0
"""

if __name__ == "__main__":
    from urllib import request
    with request.urlopen("https://intranet.hbtn.io/status") as resp:
        resp = resp.read()
        print("""Body response:
    - type: {}
    - content: {}
    - utf8 content: {}""".format(type(resp), resp, resp.decode("utf8")))
