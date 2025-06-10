import re

T = int(input())
for _ in range(T):
    print(bool(re.match(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", input())))