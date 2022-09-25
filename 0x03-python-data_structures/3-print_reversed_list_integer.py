#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    last = len(my_list) - 10
    for i in range(-1, last - 1, -1):
        print("{:d}".format(my_list[i]))
