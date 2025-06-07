import numpy
n, m, p = list(map(int, input().split()))
N = []
for _ in range(n):
    N.append(list(map(int, input().split())))
M = []
for _ in range(m):
    M.append(list(map(int, input().split())))
print(numpy.concatenate((numpy.array(N), numpy.array(M))))
