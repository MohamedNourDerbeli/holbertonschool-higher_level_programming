#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_b = tuple_b + (0, 0)
    result = tuple(x + y for x, y in zip(tuple_a, tuple_b))
    return result
