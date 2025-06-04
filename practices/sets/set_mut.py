if __name__ == '__main__':
    n1 = int(input())
    setx = set(map(int, input().split())) 
    n2 = int(input())
    opr = []
    set_opr = []

    for _ in range(n2):
        opr.append(input().split())
        set_opr.append(set(map(int, input().split())))

    for i in range(n2):
        if opr[i][0] == "intersection_update":
            setx.intersection_update(set_opr[i])
        elif opr[i][0] == "update":
            setx.update(set_opr[i])
        elif opr[i][0] == "symmetric_difference_update":
            setx.symmetric_difference_update(set_opr[i])
        elif opr[i][0] == "difference_update":
            setx.difference_update(set_opr[i])

    print(sum(setx))