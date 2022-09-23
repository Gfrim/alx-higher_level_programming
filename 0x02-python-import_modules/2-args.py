#!/usr/bin/python3
if __name__ == "__main":
    import sys
    size = len(sys.argv) - 1
    if (len(sys.argv) - 1 == 1):
        print("{} argument.".format(len(sys.argv) - 1))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(1, size + 1):
        print("{}: {}".format(i, sys.argv[i]))
