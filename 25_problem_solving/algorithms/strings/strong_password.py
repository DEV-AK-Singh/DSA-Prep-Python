#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    count = 0 
    if not any(i.isdigit() for i in password):
        count += 1
    if not any(i.islower() for i in password):
        count += 1
    if not any(i.isupper() for i in password):
        count += 1
    if not any(i in "!@#$%^&*()-+" for i in password):
        count += 1 
    return max(6 - n, count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
