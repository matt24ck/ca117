#!/usr/bin/env python3

from stack_092 import Stack

def matcher(l):
    if len(l) % 2 == 1:
        return False
    l = list(l)
    l.sort()
    l = "".join(l)
    lefts = "{[("
    rights = "}])"

    s = Stack()
    i = 0
    while i < len(l):
        if l[i] in lefts:
            s.push(l[i])
        elif l[i] in rights and len(s.l) > 0:
            s.pop()
        i += 1
    return s.is_empty()

if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        print(matcher(line.strip()))
