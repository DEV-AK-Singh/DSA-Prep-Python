if __name__ == '__main__':
    superset = set(map(int, input().split()))
    subset_arr = []
    n = int(input())
    for _ in range(n):
        subset = set(map(int, input().split()))
        subset_arr.append(subset) 
    flag = True
    for subset in subset_arr:
        if not superset.issuperset(subset):
            flag = False
            break
    if flag:
        print(True)
    else:
        print(False)    