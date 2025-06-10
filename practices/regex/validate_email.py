import email.utils as eutils 
import re
T = int(input())
regex_pattern = r"(^[a-z]{1}[a-z0-9-_.]+@[a-z]+\.[a-z]{1,3}$)"
for _ in range(T):
    name, email = eutils.parseaddr(input())
    if re.match(regex_pattern, email):
        print(eutils.formataddr((name, email)))