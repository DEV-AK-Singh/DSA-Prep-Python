# senior -> $9
# adult -> $12
# child -> $7
# discount @all -> $2 on wednesday

def movie_ticket_checker():
    age = int(input("Enter your age: "))
    day = input("Enter the day: ").lower()
    ticket_price = 0
    age_group = ""

    if age >= 65: 
        age_group = "senior"
        ticket_price = 9
    elif age >= 18:
        age_group = "adult"
        ticket_price = 12
    else:
        age_group = "child"
        ticket_price = 7

    if day == "wednesday":
        ticket_price -= 2

    print(f"You are a {age_group} and your ticket price is ${ticket_price}")

while True:
    movie_ticket_checker()
    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != "y":
        break    