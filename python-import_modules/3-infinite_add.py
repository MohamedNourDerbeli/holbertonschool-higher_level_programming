#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    s = 0
    if len(argv) <= 1:
        print("{}".format(len(argv)-1))
        exit
    for i in range(1, len(argv)):
        s += int(argv[i])
    print("{}".format(s))