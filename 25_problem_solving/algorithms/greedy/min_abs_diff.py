#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    min_abs = math.inf 
    for i in range(0, n): 
        start = i
        end = i + 1 if i + 1 < n else 0
        print(arr[start], arr[end], abs(arr[start]-arr[end]))
        min_abs = min(abs(arr[start]-arr[end]), min_abs) 
    return min_abs            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
