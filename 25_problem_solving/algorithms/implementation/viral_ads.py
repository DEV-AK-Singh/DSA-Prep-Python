#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    day = 2
    recipients = 5
    likes = 2
    cumulative = 2
    while day <= n: 
        recipients = math.floor(recipients/2) * 3
        likes = math.floor(recipients/2)
        cumulative += likes
        day += 1
    return cumulative
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
