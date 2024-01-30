#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if not roman_string:
        return 0
    s = 0
    prev = 0
    for i in roman_string[::-1]:
        if i not in roman:
            return 0
        if roman[i] >= prev or prev == roman[i]:
            s += roman[i]
        else:
            s -= roman[i]
        prev = roman[i]
    return s
