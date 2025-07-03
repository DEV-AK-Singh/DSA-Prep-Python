#!/bin/python3

import math
import os
import random
import re
import sys 
import copy

def largestPermutation(k, arr):
    indices = {a: b for b, a in enumerate(arr)}
    for i in range(len(arr)):
        if k > 0:
            if arr[i] != len(arr) - i:
                value = copy.deepcopy(arr[i])
                arr[i], arr[indices[len(arr) - i]] = len(arr) - i, arr[i]
                indices[value] = indices[len(arr) - i]
                k -= 1
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
