#!/usr/bin/python3
import sys
size = len(sys.argv) - 1
if size == 1:
    print("{} argument.".format(size))
else:
    print("{} arguments:".format(size))
    for i in range(1, size + 1):
        print("{}: {}".format(i, sys.argv[i]))
#print("{}: {}".format(sys.argv[0]))
