#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return list(filter(lambda x:x if x not in set_1 and x not in set_2 else 
None, set_1))
