#!/bin/python3

import math
import os
import random
import re
import sys
 
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    num_of_games = 0
    total_cost = 0 
    while total_cost <= s:
        total_cost += max((p - num_of_games*d), m) 
        if total_cost > s:  
            break
        num_of_games += 1
    return num_of_games

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
