#!/usr/bin/env python3

import sys
def get_roots(a, b, c):
    out = []
#    if ((b ** 2) - (4 * a * c)) > 0:
    one = -b
    two = b ** 2
    ye = -4 * a * c
    three = 2 * a
    if two + ye >= 0:
        out = [(one + (two + ye) ** 0.5) / three, (one - (two + ye) ** 0.5) / three]
    else:
        out = "None"
    return out

def main():
    lines = sys.stdin.readlines()
    for line in lines:
        a, b, c = line.strip().split()
        try:
            out1, out2 = get_roots(int(a), int(b), int(c))
            print("r1 = {}, r2 = {}".format(out1, out2))
        except ValueError:
            print(get_roots(int(a), int(b), int(c)))
main()
