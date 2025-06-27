#!/bin/python3

import math
import os
import random
import re
import sys 

def gridSearch(G, P): 
    rows_number, column_number = len(G), len(G[0])
    patterns_number, first_pattern_len = len(P), len(P[0]) 
    
    if patterns_number > rows_number or first_pattern_len > column_number:
        return "NO" 
        
    for row_i in range(rows_number): 
        rows_left = rows_number - row_i 
        if rows_left < patterns_number:
            return "NO" 
        for col_j in range(column_number - first_pattern_len + 1) : 
            if G[row_i][col_j:col_j + first_pattern_len] == P[0]: 
                matches = [
                    G[row_i + i][col_j:col_j + first_pattern_len] == P[i]
                    for i in range(patterns_number)
                ] 
                if all(matches):
                    return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
