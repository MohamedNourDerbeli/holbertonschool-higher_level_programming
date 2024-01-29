#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dic = a_dictionary.copy()
    for k, v in b_dic.items():
        b_dic[k] = v * 2
    return b_dic
