#!/usr/bin/env python3

def maximum(l):
    if len(l) == 0:
        raise ValueError('Cannot find the maximum of an empty list.')
    elif len(l) == 1:
        return l[0]
    else:
        maxNumber = maximum(l[1:])
        mymax = l[0]
        if maxNumber > mymax:
            mymax = maxNumber
        return mymax
