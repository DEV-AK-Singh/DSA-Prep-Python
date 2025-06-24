#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    ins_sort = arr.copy()
    sorted_arr = sorted(arr)
    for i in range(n):
        max_val = max(arr)
        ins_sort[n-1-i] = max_val
        arr.remove(max_val)  
        if ins_sort != sorted_arr:
            print(" ".join(list(map(str, ins_sort))))
    print(" ".join(list(map(str, sorted_arr))))
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
