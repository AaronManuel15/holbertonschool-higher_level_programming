#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 and idx not in range(len(my_list)):
        return
    return my_list[idx]
