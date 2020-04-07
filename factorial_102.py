#!/usr/bin/env python3

def factorial(n):
    cache = {}

    if n in cache:
        return cache[n]
    elif n == 0:
        value = 1
    elif n == 1:
        value = 1
    else:
        value = n * factorial(n - 1)

    cache[n] = value
    return value

if __name__ == "__main__":
    print(factorial(0))
    print(factorial(1))
    print(factorial(12))
