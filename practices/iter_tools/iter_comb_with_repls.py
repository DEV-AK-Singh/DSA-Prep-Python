from itertools import combinations_with_replacement
if __name__ == "__main__": 
    s, k = input().split() 
    print(*["".join(x) for x in sorted(list(combinations_with_replacement(sorted(s), int(k))))], sep='\n') 