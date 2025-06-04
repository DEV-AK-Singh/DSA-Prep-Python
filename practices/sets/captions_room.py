if __name__ == '__main__':
    target = int(input())
    arr = list(map(int, input().split()))
    counter_arr = {}
    for i in range(len(arr)):
        if arr[i] in counter_arr:
            counter_arr[arr[i]] += 1
        else:
            counter_arr[arr[i]] = 1
    for key in counter_arr:
        if counter_arr[key] != target:
            print(key)
            break 
        
    