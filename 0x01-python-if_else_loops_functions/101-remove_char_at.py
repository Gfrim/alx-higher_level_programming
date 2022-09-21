#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for i in str:
        if str.index(i) == n:
            continue
        else:
            new += i
    return new
