#!/bin/python3

import math
import os
import random
import re
import sys 

def gradingStudents(grades):
    final_grades = []
    for ele in grades:
        if ele < 38:
            final_grades.append(ele) 
        else:
            num = math.floor(ele / 10) * 10
            round_num = ele % 10
            num_add = 0
            if round_num == 0:
                num_add = 0
            elif round_num > 0 and round_num <= 5:
                num_add = 5
            else:
                num_add = 10
            next_5_mul = num + num_add
            final_num = next_5_mul if next_5_mul - ele < 3 else ele
            final_grades.append(final_num)
    return final_grades
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
