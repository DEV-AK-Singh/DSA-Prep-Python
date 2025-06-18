#!/bin/python3

import math
import os
import random
import re
import sys 

def repeatedString(s, n):
    full_repeats = n // len(s)
    remainder = n % len(s)
    
    a_in_full = s.count('a') * full_repeats
    a_in_partial = s[:remainder].count('a')
    
    return a_in_full + a_in_partial
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
