#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr): 
    cut_arr = []
    while len(arr)>0:
        min_val = min(arr)
        cut_arr.append(len(arr))
        arr = list(filter(lambda x:x!=min_val, arr))
        arr = list(map(lambda x:x-min(arr), arr))  
    return cut_arr
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
