#!/bin/python3

import math
import os
import random
import re
import sys 
from collections import OrderedDict

if __name__ == '__main__':
    s = sorted(str(input()))
    od = OrderedDict()
    for i in s:
        if i in od:
            od[i] += 1
        else:
            od[i] = 1
    print(*[f"{key} {value}" for key, value in sorted(od.items(), key=lambda x: x[1], reverse=True)[0:3]], sep='\n')    

