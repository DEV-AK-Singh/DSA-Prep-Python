if __name__ == '__main__':
    x, k = map(int, input().split())
    exp = eval(input())
    if exp == k:
        print(True)
    else:
        print(False)
    