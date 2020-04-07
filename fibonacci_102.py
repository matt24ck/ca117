#!/usr/bin/env python3


def fibonacci(n):
    fib_cache = {}
    if n in fib_cache:
        return fib_cache[n]
    elif n == 0:
        value = 1
    elif n == 1:
        value = 1
    elif n > 1:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    fib_cache[n] = value
    return value
