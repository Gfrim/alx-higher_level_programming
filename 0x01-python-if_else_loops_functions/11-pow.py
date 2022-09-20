#!/usr/bin/python3
def pow(a, b):
    result = a
    for i in range(b):
        if (b != 2):
            result *= a
        else:
            result = a * a
    return result
