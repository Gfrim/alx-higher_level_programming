#!/usr/bin/python3
def common_elements(set_1, set_2):
	return list(filter(lambda x:x if x in set_1 and x in set_2 else None, set_1))
