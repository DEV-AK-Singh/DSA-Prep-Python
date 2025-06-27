#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    book = [] 
    for i in range(0, n):  
        page = []
        for j in range(1, arr[i]+1):
            page.append(j)
            if (len(page) % k == 0) or (arr[i] == j):
                book.append(page)
                page = []
    special_problems = 0
    page_num = 1
    for page in book:
        if page_num in page:
            special_problems += 1
        page_num += 1
    return special_problems

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
