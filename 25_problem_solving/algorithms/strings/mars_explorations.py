#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    s = list(s)
    msg = ['S','O','S']
    i = 0
    t = 0
    lc = 0
    length = len(s)
    while t < length:
        if s[t] != msg[i%3]:
            lc += 1 
        i += 1
        t += 1  
    return lc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
