#!/bin/python3
 
import os  

# def rotateLeft(d, arr):
#     temp = None
#     for i in range(d):
#         temp = arr[0]
#         for j in range(len(arr) - 1):
#             arr[j] = arr[j + 1]
#         arr[len(arr) - 1] = temp
#     return arr

def rotateLeft(d, arr):
    return arr[d:] + arr[:d]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
