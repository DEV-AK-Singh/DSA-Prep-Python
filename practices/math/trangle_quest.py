if __name__ == '__main__':
    size = int(input())
    for i in range(1, size + 1):
        # print([ele * pow(10, idx) for idx, ele in enumerate(list([x for x in range(1, i + 1)] + [y for y in range(i-1, 0, -1)]))])
        print(''.join([str(x * pow(10, idx)) for idx, x in enumerate(list([x for x in range(1, i + 1)] + [y for y in range(i-1, 0, -1)]))]))