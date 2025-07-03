#!/bin/python3

import math
import os
import random
import re
import sys  

def decentNumber(n):
    fives = n
    threes = 0 
    while fives >= 0:
        if fives % 3 == 0 and threes % 5 == 0:
            break
        else:
            fives -= 1
            threes += 1
    print(-1 if fives < 0 else ('5' * fives) + ('3' * threes))
    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
