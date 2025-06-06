from itertools import groupby 
if __name__ == "__main__": 
    s = str(input())
    for k, g in groupby(s):
        print(f"({len(list(g))}, {k})", end=" ")