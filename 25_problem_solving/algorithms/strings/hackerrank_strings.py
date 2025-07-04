#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    s = list(s)
    n = len(s)
    i = 0
    hr = list('hackerrank')
    m = len(hr)
    j = 0
    while i < n:
        if hr[j] == s[i]:
            j += 1
        i += 1
        if j == m:
            return "YES"
    return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
