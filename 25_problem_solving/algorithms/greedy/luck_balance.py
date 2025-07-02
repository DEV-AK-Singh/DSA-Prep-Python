#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    total = sum([x[0] for x in contests]) 
    sorted_imp_con = sorted(filter(lambda x: x[1]==1 , contests))[::-1]
    unsorted_imp_con = sorted(filter(lambda x: x[1]==0 , contests)) 
    if k < len(sorted_imp_con):
        luck_pos = unsorted_imp_con + sorted_imp_con[:k]
        luck_neg = sorted_imp_con[k:]
        return sum([x[0] for x in luck_pos]) - sum([x[0] for x in luck_neg])
    else:
        return total 
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
