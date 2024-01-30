#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    no_str = [x for x in my_list if not isinstance(x, str)]
    for i in range(x):
        try:
                print("{:d}".format(no_str[i]), end="")
                count += 1
        except TypeError:
            break

    print()
    return count
