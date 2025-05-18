def age_grp_checker():
    user_age = int(input("Enter your age: "))

    if user_age >= 65:
        print("You are a senior")    
    elif user_age >= 18:
        print("You are an adult")
    elif user_age >= 13:
        print("You are a teenager")
    else:
        print("You are a child")


while True:
    age_grp_checker()
    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != "y":
        break