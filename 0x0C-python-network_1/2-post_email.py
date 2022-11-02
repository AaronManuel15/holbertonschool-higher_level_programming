#!/usr/bin/python3
""" Task 2
"""

if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv
    
    parameter = {'email': argv[2]}
    data = parse.urlencode(parameter)
    data = data.encode()
    req = request.urlopen(argv[1], data)
    with request.urlopen(req) as resp:
        print(resp.read().decode('utf8'))
