from collections import defaultdict
if __name__ == "__main__":
    d = defaultdict(list)
    A, B = map(int, input().split())
    for i in range(A):
        d[input()].append(i + 1)
    for i in range(B):
        key = input()
        if key in d:
            print(*d[key])
        else:
            print(-1)
            
