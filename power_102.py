#!/usr/bin/env python3

def power(n, m):
    if m == 0:
        value = 1
    elif m == 1:
        value = n
    elif m > 1:
        value = n ** m
    else:
        value = power(n, m - 1)
    return value
