#!/usr/bin/python3
"""Project 0x08. Python - Input/Output
Task 7
"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """script that adds all arguments to a Python list
    and then save them to a file
    """

    from sys import argv
    try:
        lst = (load_from_json_file('add_item.json'))
    except FileNotFoundError:
        lst = []
    save_to_json_file(lst + argv[1:], 'add_item.json')

if __name__ == "__main__":
    main()
