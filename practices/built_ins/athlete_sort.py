if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    k = int(input()) 
    print(*[" ".join(map(str, i)) for i in sorted(arr, key=lambda x: x[k])], sep='\n')