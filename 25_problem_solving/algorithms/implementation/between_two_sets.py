#!/bin/python3

import math
import os
import random
import re
import sys
 
def breakingRecords(scores):
    maxRecBreakCnt = 0
    minRecBreakCnt = 0
    maxVal = scores[0]
    minVal = scores[0]
    for rec in scores:
        if rec > maxVal:
            maxVal = rec
            maxRecBreakCnt+=1
        elif rec < minVal:
            minVal = rec
            minRecBreakCnt+=1    
    return [maxRecBreakCnt, minRecBreakCnt]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
