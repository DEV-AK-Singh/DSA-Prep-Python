#!/bin/python3

import math
import os
import random
import re
import sys 

def gridChallenge(grid):
    grid = [sorted(s) for s in grid]    
    for c in range(len(grid[0])):
        c_str = [row[c] for row in grid] 
        for i in range(1, len(c_str)):
            if c_str[i-1] > c_str[i]:
                return "NO" 
    return "YES" 
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
