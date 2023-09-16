#!/usr/bin/env python3

def print_fibonacci(length):
    my_list = []
    for i in range(length):
        if i == 0:
            my_list.append(0)
        elif i == 1:
            my_list.append(1)
        else:
            sum = my_list[i-2] + my_list[i-1]
            my_list.append(sum)
    print(my_list)
