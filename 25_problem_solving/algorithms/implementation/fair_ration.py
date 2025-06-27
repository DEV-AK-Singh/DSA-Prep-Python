#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(arr):
    loaves = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            pass
        elif i != len(arr)-1:
            arr[i] += 1
            if i + 1 < len(arr):    
                arr[i+1] += 1
                loaves += 2
    if arr[len(arr)-1] % 2 == 0:
        return str(loaves)
    else:
        return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
