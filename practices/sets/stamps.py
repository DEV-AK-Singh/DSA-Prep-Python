if __name__ == "__main__":
    stamps = set()
    n = int(input())
    for _ in range(n):
        stamps.add(str(input()))
    print(len(list(stamps)))