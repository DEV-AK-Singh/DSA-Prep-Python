#!/bin/python3

import math
import os
import random
import re
import sys
 
def acmTeam(topic):
    total_attendee = len(topic)
    total_topics = len(topic[0]) 
    teams = []
    counts = []
    max_val = -1
    for i in range(0, total_attendee):
        for j in range(i+1, total_attendee):
            teams.append([i,j])
    for team in teams:
        a = list(topic[team[0]])
        b = list(topic[team[1]])
        count = 0
        for i in range(total_topics):
            if a[i] == '0' and b[i] == '0':
                continue
            else:
                count += 1
        max_val = max(count, max_val)
        counts.append(count)
    return [max_val, counts.count(max_val)]
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
