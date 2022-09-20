#!/usr/bin/python3
def pow(a, b):
    result = a
    for i in range(b):
        if b != 2:
            result *= a
        elif b < 0:
            result *= 1 / a
        elif b == 0:
            result = 1
        else:
            result = a * a
    return result
