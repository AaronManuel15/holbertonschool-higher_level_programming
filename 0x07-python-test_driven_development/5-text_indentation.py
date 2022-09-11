#!/usr/bin/python3
"""
    Project 0x05 - Test driven development
    Task 4
    prints a text with 2 new lines after characters
"""


def text_indentation(text):
    """
        Adds two lines after each '.', '?', and ':'.

        Args:
            text: _description_
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    newString1 = text.replace(". ", "\n\n")
    newString2 = newString1.replace(".", "\n\n")
    newString3 = newString2.replace("? ", "\n\n")
    newString4 = newString3.replace("?", "\n\n")
    newString5 = newString4.replace(": ", "\n\n")
    newString6 = newString5.replace(":", "\n\n")
    print(newString6)
