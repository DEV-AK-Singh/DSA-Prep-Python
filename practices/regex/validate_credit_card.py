import re
n = int(input())
for _ in range(n):
    u = str(input())
    try:
        assert re.search(r"^[4-6]", u) 
        assert bool(re.match(r"^\d{16}$", u)) or bool(re.match(r"^\d{4}-\d{4}-\d{4}-\d{4}$", u)) 
        if '-' in u:
            u = u.replace('-', '')
        assert not re.search(r'(\d)\1{3}', u)
    except:
        print("Invalid")
    else:
        print("Valid")
