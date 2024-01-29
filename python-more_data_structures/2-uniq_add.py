#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = 0
    new_list = list(set(my_list))
    for i in new_list:
        s += i
    return s
