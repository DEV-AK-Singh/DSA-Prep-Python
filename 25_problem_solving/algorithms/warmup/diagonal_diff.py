#!/bin/python3

import math
import os
import random
import re
import sys 

def diagonalDifference(arr):
    n = len(arr)
    d1 = 0
    d2 = 0
    for i in range(n): 
        d1 += arr[i][i]
        d2 += arr[i][n-1-i]
    return abs(d1-d2)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
