import numpy
arr = []
n, m = list(map(int, input().split()))
for _ in range(n):
    arr.append(list(map(int, input().split())))
numpy_arr = numpy.array(arr)
print(numpy.transpose(numpy_arr))
print(numpy_arr.flatten())      
