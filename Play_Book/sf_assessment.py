#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balance' function below.
#
# The function accepts STRING_ARRAY arr as parameter.
#

open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

def balance(arr):
    stack = []
    for i in arr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                print("Not Valid")
    if len(stack) == 0:
        print("Valid")
    else:
        print("Not Valid")

if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = []
    for _ in range(arr_count):
        arr_item = input()
        arr.append(arr_item)
    balance(arr)
