#!/usr/bin/env python3

def minimum(l):
    if len(l) == 0:
        raise ValueError('Cannot find the minimum of an empty list.')
    elif len(l) == 1:
        return l[0]
    else:
        minNumber = minimum(l[1:])
        mymin = l[0]
        if minNumber < mymin:
            mymin = minNumber
        return mymin
