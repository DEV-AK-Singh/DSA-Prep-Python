#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#

def toys(W):
    W = sorted(W) 
    max_weight = W[0] + 4
    cnt = 1
    for w in W:
        if w > max_weight:
            cnt += 1
            max_weight = w + 4 
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
