#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Create a dictionary to map value to its 1-based index
    value_to_index = {val: i+1 for i, val in enumerate(p)}
    
    # For each x from 1 to n, find y where p[p[y]] = x
    result = []
    for x in range(1, len(p)+1):
        # First find the index where p[k] = x
        k = value_to_index[x]
        # Then find the index where p[j] = k
        j = value_to_index[k]
        result.append(j)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
