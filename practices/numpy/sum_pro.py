import numpy as np
n, m = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
my_arr = np.array(arr)
print(np.prod(np.sum(my_arr, axis=0)))