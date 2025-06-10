import re
n = int(input())
for _ in range(n):
    u = str(input())
    setData = set(u)
    u = ''.join(sorted(u)) 
    try:
        assert re.search(r"[A-Z]{2}", u)
        assert re.search(r"\d\d\d", u)
        assert re.search(r"^[0-9a-zA-Z][0-9a-zA-Z]+[0-9a-zA-Z]$", u)  
        assert len(setData) == len(u) == 10
    except:
        print("Invalid")
    else:
        print("Valid")    