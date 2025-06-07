import numpy as np
n, m = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
my_arr = np.array(arr)
print(np.mean(my_arr, axis=1))
print(np.var(my_arr, axis=0))
print(np.std(my_arr, dtype=np.float32))