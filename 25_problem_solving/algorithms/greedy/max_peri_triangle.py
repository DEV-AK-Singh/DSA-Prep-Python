#!/bin/python3

import math
import os
import random
import re
import sys 

def checkTriangle(a, b, c):
    return all([a+b>c, a+c>b, b+c>a])

def maximumPerimeterTriangle(sticks):
    n = len(sticks)
    max_val = 0
    max_triple = [-1]
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n): 
                if checkTriangle(sticks[i], sticks[j], sticks[k]):
                    if max_val < sticks[i]+sticks[j]+sticks[k]:
                        max_val = sticks[i]+sticks[j]+sticks[k]
                        max_triple = [sticks[i], sticks[j], sticks[k]]
    return sorted(max_triple)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
