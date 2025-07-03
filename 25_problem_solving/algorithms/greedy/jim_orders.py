#!/bin/python3

import math
import os
import random
import re
import sys
 
def jimOrders(orders):
    for i in range(len(orders)):
        orders[i].append(orders[i][0]+orders[i][1])
        orders[i].append(i+1)
    sorted_orders = sorted(orders, key=lambda x: x[2])
    return [x[-1] for x in sorted_orders]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
