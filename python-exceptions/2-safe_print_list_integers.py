#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    no_str = [x for x in my_list if not isinstance(x, str)]
    try:
        for i in range(x):
            print("{:d}".format(no_str[i]), end="")
            count += 1
        print("")
        return count
    except TypeError:
        pass
    print()
    return count
