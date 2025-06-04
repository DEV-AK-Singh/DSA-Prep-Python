# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    oprs = []
    n1 = int(input())
    s1 = set(map(int, input().split()))
    n2 = int(input())
    for _ in range(n2):
        oprs.append(input().split())
    for opr in oprs:
        if opr[0] == "pop" and len(list(s1)) > 0:
            s1.pop()
        elif opr[0] == "remove" and int(opr[1]) in s1:
            s1.remove(int(opr[1]))
        elif opr[0] == "discard":
            s1.discard(int(opr[1]))
    print(sum(s1))