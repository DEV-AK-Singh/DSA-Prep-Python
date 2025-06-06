# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    cubes = deque(map(int, input().split()))

    last = float('inf')
    possible = True

    while cubes:
        
        if cubes[0] >= cubes[-1] and cubes[0] <= last:
            last = cubes.popleft()
        elif cubes[-1] >= cubes[0] and cubes[-1] <= last:
            last = cubes.pop()
        else:
            possible = False
            break

    print("Yes" if possible else "No")