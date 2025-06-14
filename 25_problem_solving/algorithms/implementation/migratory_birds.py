#!/bin/python3

import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    birds = {} 
    birds_id = []
    for bird in arr:
        if bird in birds:
            birds[bird] += 1
        else:
            birds[bird] = 1
    max_spot = max(birds.values())
    for key, val in birds.items():
        if val == max_spot:
            birds_id.append(key)
    return sorted(birds_id)[0]                  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
