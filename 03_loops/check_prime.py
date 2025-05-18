def check_prime(n):
    is_prime = True 
    for i in range(2, n): 
        if n % i == 0:
            is_prime = False
            break
    return is_prime        

while True:
    n = int(input("Enter a number: "))
    if check_prime(n):
        print(f"{n} is a prime number")
        break
    else:
        print(f"{n} is not a prime number try again")