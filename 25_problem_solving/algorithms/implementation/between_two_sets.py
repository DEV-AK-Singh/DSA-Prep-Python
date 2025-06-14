#!/bin/python3

import math
import os
import random
import re
import sys 

def getTotalX(a, b):
    max_a = max(a)
    min_b = min(b)
    
    if max_a > min_b:
        return 0
    
    count = 0
    for x in range(max_a, min_b + 1):
        if all(x % num == 0 for num in a) and all(num % x == 0 for num in b):
            count += 1
    
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
