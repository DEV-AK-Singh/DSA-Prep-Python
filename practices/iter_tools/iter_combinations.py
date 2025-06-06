from itertools import combinations
if __name__ == "__main__": 
    s, k = input().split() 
    for i in range(1, int(k) + 1):
        print(*["".join(x) for x in sorted(list(combinations(sorted(s), i)))], sep='\n')