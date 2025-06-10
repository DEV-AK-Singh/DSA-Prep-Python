# import re
# if __name__ == "__main__": 
#     pattern = r".+:{1}.*(\#{1}[A-Fa-f0-9]{6}|[A-Fa-f0-9]{3}).*"
#     for _ in range(int(input())):
#         print((re.findall(pattern, input())))

import re
N=int(input())

for i in range(0,N):
    s=input()

    x=s.split()

    if len(x)>1  and  '{' not in x:
        x=re.findall(r'#[a-fA-F0-9]{3,6}',s)
        [print(i) for i in x]