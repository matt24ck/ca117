#!/usr/bin/env python3
from re import findall


date = r'\b\d+[/-]\d+[/-]\d+\b'
phone = r'\b\d{2}[-\s]\d{7}\b'
email = r'\b(?:\w+\.)*\w+\@\w+\.\w+(?:\.\w+)*\b'
ldate = r'\b\d{2}[\s/-]\w{3}[\s/-]\d{2}\b'

if __name__ == "__main__":
    with open("test.txt") as f:
        s = f.read()
    print(findall(date, s))
    print(findall(phone, s))
    print(findall(email, s))
    print(findall(ldate, s))
