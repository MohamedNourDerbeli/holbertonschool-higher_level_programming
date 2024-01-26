#!/usr/bin/python3
def max_integer(my_list=[]):
    result = 0
    if my_list is None:
        return None
    else:
        for max in range(0, len(my_list) - 1):
            if result < my_list[max + 1]:
                result = my_list[max + 1]
        return result
