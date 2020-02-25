#!/usr/bin/env python3

def swap_keys_values(d):
    a = []
    b = []
    for key in d:
        if d[key] in b:
            b.append(0)
        else:
            a.append(d[key])
            b.append(key)
        new_d = {}
        i = 0
    while i < len(a):
        new_d[b[i]] = a[i]
        i += 1
    return new_d

if __name__ == "__main__":
    dic = {'a': 4, 'b': 7, 'c': 10, 'd': 7}
    print(swap_keys_values(dic))
