#!/usr/bin/env python3

def sumup(n):
    cache = {}

    if n in cache:
        return cache[n]
    elif n == 0:
        value = 0
    elif n == 1:
        value = 1
    else:
        value = n + sumup(n - 1)

    cache[n] = value
    return value

if __name__ == "__main__":
    print(sumup(0))
    print(sumup(1))
    print(sumup(12))
