#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s = 0
    if not roman_string or roman_string is int:
        return 0
    for i in roman_string[::-1]:
        if i in roman:
            s += roman[i]
    return s
