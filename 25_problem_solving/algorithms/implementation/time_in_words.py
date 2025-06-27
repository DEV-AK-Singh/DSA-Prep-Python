#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m): 
    hours = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
    minutes = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","twenty one","twenty two","twenty three","twenty four","twenty five","twenty six","twenty seven","twenty eight","twenty nine"]
    if m == 0:
        return hours[h-1] + " o' clock"
    if m == 1:
        return "one minute past " + hours[h-1]
    if m == 15:
        return "quarter past " + hours[h-1]
    if m == 30:
        return "half past " + hours[h-1]
    if m == 45:
        return "quarter to " + hours[h]
    if m < 30:
        return minutes[m-1] + " minutes past " + hours[h-1]
    return minutes[60-m-1] + " minutes to " + hours[h]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
