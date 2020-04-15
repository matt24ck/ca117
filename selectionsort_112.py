#!/usr/bin/env python

def selectionsort(a):
    i = 0
    while i < len(a):
        j = i + 1
        p = i
        while j < len(a):
            if a[j] < a[p]:
                p = j
            j += 1

        tmp = a[i]
        a[i] = a[p]
        a[p] = tmp
        i += 1

import random
def main():
    A = random.sample(range(-99, 100), 10)

    print('Unsorted: {}'.format(A))
    selectionsort(A)
    print('Sorted: {}'.format(A))

if __name__ == '__main__':
    main()
