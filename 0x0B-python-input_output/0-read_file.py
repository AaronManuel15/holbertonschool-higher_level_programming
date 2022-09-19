#!/usr/bin/python3
""" Project 0x08. Python - Input/Output
    Task 0
"""


def read_file(filename=""):
    """Program that eads a text file (UTF8) and prints it to stdout
    """
    with open(filename, encoding="utf=8") as file:
        fileText = file.read()
        print(fileText, end="")
