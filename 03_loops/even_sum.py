n = input("Enter a number: ")
sum = 0

for i in range(1, int(n) + 1):
    if i % 2 == 0:
        sum += i

print(sum)    