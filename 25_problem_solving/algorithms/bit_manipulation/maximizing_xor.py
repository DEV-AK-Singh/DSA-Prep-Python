#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximizingXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def maximizingXor(l, r):
    a = [ele for ele in range(l, r+1)]
    b = [ele for ele in range(l, r+1)]
    max_xor = 0
    for ele_a in a:
        for ele_b in b:
            xor_val = ele_a ^ ele_b
            max_xor = max(max_xor, xor_val)
    return max_xor

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
