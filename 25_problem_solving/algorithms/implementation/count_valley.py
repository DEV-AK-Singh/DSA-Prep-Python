#!/bin/python3

import math
import os
import random
import re
import sys 

def countingValleys(steps, path):
    # Write your code here
    countUpDown = 0
    countValley = 0
    for step in path:
        if step == "U":
            countUpDown += 1 
            if countUpDown == 0:
                countValley += 1
        else:
            countUpDown -= 1
    return countValley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
