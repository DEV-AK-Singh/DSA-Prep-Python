#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy = 100
    start = 0
    end = len(c) - 1
    curr = start 
    flag = False
    while curr != start or flag is False:
        flag = True
        if curr > end:
            curr -= end+1 
            if curr == start:
                break
        energy -= 1
        if c[curr] == 1:
            energy -= 2
        print(curr)
        curr += k
    return energy
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
