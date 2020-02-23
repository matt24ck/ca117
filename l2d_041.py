#!/usr/bin/env python3

import sys
def l2d(f):
    a, b = f.readlines()
    a = a.strip().split()
    b = b.strip().split()
    myDic = {}
    i = 0
    while i < len(a):
        myDic[a[i]] = int(b[i])
        i += 1
    return myDic

if __name__ == "__main__":
    f = open("test.txt")
    l2d(f)
    f.close()
