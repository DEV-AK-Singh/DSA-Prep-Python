import re
N, M = input().split()

matrix = []
coded_string = ""

for _ in range(int(N)):
    matrix.append(list(input()))

for i in range(int(M)):
    for j in range(int(N)):
        coded_string += matrix[j][i]

print(re.sub('(?<=[a-zA-Z0-9_])[!@#$%&" "]+(?=[a-zA-Z0-9_])', " ", coded_string))