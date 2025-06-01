import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result
    return wrapper

@time_it
def binary_search(arr, target):
    left_idx = 0
    right_idx = len(arr) - 1
    while left_idx <= right_idx:
        min_idx = left_idx + (right_idx - left_idx) // 2
        if arr[min_idx] == target:
            return min_idx
        elif arr[min_idx] < target:
            left_idx = min_idx + 1
        else:
            right_idx = min_idx - 1
    return -1

@time_it
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
 
def binary_search_recur(arr, target, left_idx, right_idx):
    if left_idx > right_idx:
        return -1
    min_idx = left_idx + (right_idx - left_idx) // 2
    if arr[min_idx] == target:
        return min_idx
    elif arr[min_idx] < target:
        return binary_search_recur(arr, target, min_idx + 1, right_idx)
    else:
        return binary_search_recur(arr, target, left_idx, min_idx - 1)
    
@time_it    
def bin_search(arr, target, left_idx, right_idx):
    return binary_search_recur(arr, target, left_idx, right_idx)    

def main():
    arr = [num for num in range(1000000)]
    target = 999999
    print(binary_search(arr, target))
    print(linear_search(arr, target))
    print(bin_search(arr, target, 0, len(arr) - 1))

if __name__ == "__main__": 
    main()