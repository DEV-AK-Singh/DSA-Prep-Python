def isPalindrome(s):
    return str(s) == str(s)[::-1]

def isPositive(n):
    return n > 0

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(all(map(isPositive, arr)) and any(map(isPalindrome, arr)))

    