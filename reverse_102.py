#!/usr/bin/env python3

def reverse_list(l):
    if len(l) == 0:
        return l
    else:
        return [l[-1]] + reverse_list(l[:-1])
