#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if (idx == my_list.index(i)):
            idx = i
        elif (idx < 0 or idx > len(my_list) - 1):
            return None
    return idx
