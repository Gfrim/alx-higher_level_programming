#!/usr/bin/python3
for i in range(9):
    for i in range(10):
        if (i == j or i < j):
            continue
        elif (i == 8 and j and 9):
            print(f"{i:d}{j:d}")
        else:
            print(f"{i:d}{j:d}", end=", ")
