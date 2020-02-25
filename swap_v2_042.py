#!/usr/bin/env python3

def swap_unique_keys_values(d):
    a = []
    b = []
    for key in d:
        if d[key] in a:
            a.append(0)
            b[a.index(d[key])] = 0
            a[a.index(d[key])] = 0
            b.append(0)
        else:
            a.append(d[key])
            b.append(key)
    new_d = {}
    i = 0
    while i < len(a):
        if a[i] != 0:
            new_d[a[i]] = b[i]
        i += 1
    return new_d
