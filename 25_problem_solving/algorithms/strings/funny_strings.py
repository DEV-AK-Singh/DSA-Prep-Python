#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    s = [ord(char) for char in s] 
    r = s[::-1]
    s_diff = []
    r_diff = []
    for i in range(1, len(s)):
        s_diff.append(abs(s[i]-s[i-1]))
        r_diff.append(abs(r[i]-r[i-1]))
    return "Funny" if s_diff == r_diff else "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
