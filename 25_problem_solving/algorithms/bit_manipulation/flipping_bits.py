#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def binaryToDecimal(bits):
    bits = list(bits)
    n = len(bits)
    decimal_value = 0
    for i in range(n-1, -1, -1): 
        decimal_value += (pow(2, i)*int(bits[n-1-i]))
    return decimal_value

def flippingBits(n):
    bin_num = bin(n).replace('b','') 
    list_digit = list(bin_num)
    if len(list_digit) < 32:
        list_digit = list((32-len(list_digit))*'0') + list_digit  
    if len(list_digit) > 32:
        list_digit = list_digit[len(list_digit)-32:]
    for i in range(0, len(list_digit)):
        list_digit[i] = '0' if list_digit[i] == '1' else '1'
    changed_bin = "".join(list_digit)  
    return binaryToDecimal(changed_bin)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
