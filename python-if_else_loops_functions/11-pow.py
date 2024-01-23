#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / pow(a, -b)
    elif b % 2 == 0:
        half_pow = pow(a, b // 2)
        return half_pow * half_pow
    else:
        half_pow = pow(a, b // 2)
        return a * half_pow * half_pow
