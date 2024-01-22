#!/usr/bin/python3
for i in range(0, 10):
    for k in range(1, 10):
        if i != k and i < k and (str(i) + str(k)) != "89":
            print("{}, ".format(str(i) + str(k)), end="")
        if (str(i) + str(k)) == "89":
            print("{}".format(str(i)+str(k)))
