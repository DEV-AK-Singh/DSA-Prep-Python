#!/bin/python3

import math
import os
import random
import re
import sys 

def stringConstruction(s):
    # Write your code here
    p = ""
    cost = 0
    for char in s:
        if p.find(char) != -1:
            cost += 0
        else:
            cost += 1
        p += char
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
