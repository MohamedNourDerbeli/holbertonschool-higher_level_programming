#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for div in range(0, len(my_list)):
        if my_list[div] % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result