#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0
    count = 0
    lastDigit = 0
    romanNumeral = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
    for x in roman_string:
        if lastDigit != 0 and lastDigit < romanNumeral[x]:
            count -= lastDigit
        else:
            count += lastDigit
        lastDigit = romanNumeral[x]
    count += lastDigit
    return count
