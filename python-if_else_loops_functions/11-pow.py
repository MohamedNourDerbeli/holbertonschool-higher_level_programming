#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    if a < 0 and b % 2 == 0:
        return (-1) * (abs(a) ** b)
    else:
        return a ** b
