#!/usr/bin/env python3


import sys

def main():
    lines = sys.stdin.readlines()
    a = lines[0].strip().split()
    i = 0
    while i < len(a):
        a[i] = int(a[i])
        i += 1
    b = lines[1].strip().split()
    i = 0
    while i < len(b):
        b[i] = int(b[i])
        i += 1
    c = lines[2].strip().split()
    i = 0
    while i < len(c):
        c[i] = int(c[i])
        i += 1

    lenab = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
    lenac = ((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2) ** 0.5
    if lenab > lenac:
        point = c
    elif lenab == lenac:
        point = a
    else:
        point = b
    pointa = [a[0] - point[0], a[1] - point[1]]
    pointb = [b[0] - point[0], b[1] - point[1]]
    pointc = [c[0] - point[0], c[1] - point[1]]
    if pointa != [0, 0] and pointc != [0, 0]:
        x = pointa[0] + c[0]
        y = pointa[1] + c[1]
    elif pointa != [0, 0] and pointb != [0, 0]:
        x = pointa[0] + b[0]
        y = pointa[1] + b[1]
    elif pointb != [0, 0] and pointc != [0, 0]:
        x = pointb[0] + c[0]
        y = pointb[1] + c[1]

    print(x, y)

if __name__ == "__main__":
    main()
