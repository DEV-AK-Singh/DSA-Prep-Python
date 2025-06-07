if __name__ == '__main__':
    s = input()
    odd = []
    even = []
    low = []
    upper = []
    for i in s:
        if i.isalpha():
            if i.islower():
                low.append(i)
            else:
                upper.append(i)
        else:
            if int(i)%2 == 0:
                even.append(i)
            else:
                odd.append(i)
    print("".join(sorted(low) + sorted(upper) + sorted(odd) + sorted(even)))
    