#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    set_arr = set(list(a))
    min_dis = len(a) + 1
    for ele in set_arr:
        pair_arr = list(filter(lambda i: a[i]==ele, range(len(a))))
        if len(pair_arr) > 1:
            min_dis = min(min_dis, pair_arr[-1]-pair_arr[0])
    return min_dis if min_dis < len(a) + 1 else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
