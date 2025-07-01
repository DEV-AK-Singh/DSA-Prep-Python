#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    l1 = len(s1)
    l2 = len(s2)
    cnt = 0
    for char in s1:
        if char in s2:
            s2.remove(char)
            cnt += 1
    return l1 + l2 - (2 * cnt)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
