import numpy as np
m = int(input())
A = np.array([input().split() for _ in range(m)], int)
B = np.array([input().split() for _ in range(m)], int)
print(np.dot(A, B)) 