#!/bin/python3

import math
import os
import random
import re
import sys 

def isValid(s):
    counts_dict = {}
    for c in s:
        counts_dict[c] = counts_dict.get(c,0) + 1
    
    counts = counts_dict.values()
    counts_len = len(counts)
    min_num = min(counts)
    max_num = max(counts)
    counts_sum = sum(counts)
    
    return "YES" if min_num*counts_len == counts_sum or min_num*counts_len+1 == counts_sum or max_num*(counts_len-1)+1==counts_sum else "NO"
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
