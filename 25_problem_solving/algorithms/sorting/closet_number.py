#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    
    sorted_arr = sorted(arr)
    
    od = OrderedDict()
    
    for i in range(1, n):
        prev = sorted_arr[i-1]
        curr = sorted_arr[i]
        od[(prev, curr)] = curr - prev
    
    min_diff = sorted(od.items(), key=lambda item: item[1])[0][1]
    
    res_arr = []
    
    for k, v in od.items():
        if min_diff == v:
            res_arr.append(k[0])
            res_arr.append(k[1])
    
    return res_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
