if __name__ == '__main__':
    itr = int(input())
    for i in range(itr):
        try:
            a, b = map(int, input().split())
            print(a//b)
        except Exception as e:
            print("Error Code:", e)