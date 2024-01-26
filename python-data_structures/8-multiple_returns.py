#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == None or sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])
