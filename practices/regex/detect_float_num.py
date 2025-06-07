if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = str(input())
        if s == '0':
            print(False)
            continue
        if s.count('.') > 1:
            print(False)
            continue
        else:
            try:
                float(s)
                print(True)
            except:
                print(False)