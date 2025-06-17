#!/bin/python3

import math
import os
import random
import re
import sys

def queensAttack(n, k, r_q, c_q, obstacles): 
    count_step = 0 
    directions = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]] 
    obstacles = set(map(tuple, obstacles)) 
    for direction in directions:
        row_dir = direction[0]
        col_dir = direction[1]
        curr_r_pos = r_q
        curr_c_pos = c_q 
        while True:
            curr_c_pos += col_dir
            curr_r_pos += row_dir
            if curr_c_pos > n or curr_c_pos < 1 or curr_r_pos > n or curr_r_pos < 1:
                break
            if (curr_r_pos, curr_c_pos) in obstacles:
                break 
            count_step += 1   
    
    return count_step
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
