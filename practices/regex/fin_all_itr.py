import re    
if __name__ == "__main__":
    s = input()
    grps = re.findall(r"[^aeiouAEIOU]([aeiouAEIOU]{2,})[^aeiouAEIOU]", s)
    if len(grps) > 0:
        print("\n".join(grps))
    else:
        print(-1)