#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    mat = [list(map(int, x)) for x in grid]
    if len(mat) <= 2:
        return ["".join(map(str, x)) for x in mat]
    cavity = []
    for i in range (1, len(mat)-1):
        for j in range(1, len(mat)-1):
            cur_r = i
            cur_c = j
            curr = mat[cur_r][cur_c]
            up = mat[cur_r - 1][cur_c]
            right = mat[cur_r][cur_c + 1]
            down = mat[cur_r + 1][cur_c]
            left = mat[cur_r][cur_c - 1]
            if all([curr>up, curr>right, curr>down, curr>left]):
                cavity.append([i,j])
    for idx in cavity:
        i = idx[0]
        j = idx[1]
        mat[i][j] = 'X'
    return ["".join(map(str, x)) for x in mat]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
