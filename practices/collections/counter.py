from collections import Counter
if __name__ == "__main__": 
    s_total = int(input())
    shoe_sizes = Counter(list(map(int, input().split())))
    person = int(input())
    money = 0
    for _ in range(person):
        size, price = map(int, input().split())
        if shoe_sizes[size] > 0:
            money += price
            shoe_sizes[size] -= 1
    print(money)