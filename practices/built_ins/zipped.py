if __name__ == "__main__":
    N, X = list(map(int, input().split()))
    Zip = zip(*[input().split() for _ in range(X)])
    for i in Zip:
        print(sum(map(float, i))/len(i))
     