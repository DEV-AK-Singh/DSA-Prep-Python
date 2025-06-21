#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k): 
    if len(t) + len(s) <= k:
        return 'Yes'
    
    index=0
		
    while True: 
        if index > len(s) - 1 or index > len(t) - 1:
            break 
        if s[index] == t[index]:
            index+=1
        else:
            break 
     
    remaining_steps = len(s) + len(t) - index * 2
    if remaining_steps <= k and (k - remaining_steps) % 2 == 0:
        return 'Yes'
    else:
        return 'No'
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
