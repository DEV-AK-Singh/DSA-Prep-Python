import math
if __name__ == '__main__':
    AB = int(input())
    BC = int(input())
    MX = BY = BC/2
    MY = BX = AB/2  
    THETA = round(math.degrees(math.atan(MY/BY)))
    print(f"{THETA}\u00B0")