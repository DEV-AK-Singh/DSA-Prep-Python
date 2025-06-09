import re
nums = int(input())
for _ in range(nums):
    num = input()
    if re.match(r"^[789]\d{9}$", num):
        print("YES")
    else:
        print("NO")