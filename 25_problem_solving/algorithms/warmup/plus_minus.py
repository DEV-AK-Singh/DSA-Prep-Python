#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    n = len(arr)
    for ele in arr:
        if ele == 0:
            zero += 1
        elif ele > 0:
            pos += 1
        elif ele < 0:
            neg += 1
    print("{:6f}".format(pos/n))
    print("{:6f}".format(neg/n))
    print("{:6f}".format(zero/n))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
