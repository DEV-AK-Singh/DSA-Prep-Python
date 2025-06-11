#!/bin/python3
 
import os 

def dynamicArray(n, queries):
    ans_arr = []
    arr = [[] for _ in range(n)]
    for i in range(len(queries)):
        query_type = queries[i][0]
        x = queries[i][1]
        y = queries[i][2]
        last_answer = 0 if len(ans_arr) == 0 else ans_arr[-1]
        idx = (x ^ last_answer) % n
        if query_type == 1:
            arr[idx].append(y)
        else:
            last_answer = arr[idx][y % len(arr[idx])]
            ans_arr.append(last_answer)
    return ans_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
