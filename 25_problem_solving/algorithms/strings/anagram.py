#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
# 

def anagram(s):
    s = list(s)
    mid = len(s)//2
    if len(s) % 2 != 0:
        return -1 
    s1 = s[0:mid]
    s2 = s[mid:] 
    for char in s1:
        if char in s2:
            s2.remove(char)
    return len(s2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
