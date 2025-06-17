#!/bin/python3

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    # Write your code here
    temp = {}
    
    for i in a:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1
            
    longest_subarray_length = 0   
    for key in temp:
        total = temp.get(key) + temp.get(key + 1, 0)
        if total > longest_subarray_length:
            longest_subarray_length = total
            
    return longest_subarray_length
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
