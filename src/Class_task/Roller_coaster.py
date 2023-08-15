height = float(input("What is your height? "))
age = 0
if height < 6:
    print("Too short, come back when you're taller. ")
elif height > 6:
    age = int(input("What is your age? "))
    if age < 12:
        print("Pay $1 for the ride. ")
    elif 12 < age <= 65:
        print("Pay $2 for the ride. ")
    elif age > 65:
        print("Your ride is absolutely free!!! ")
    else:
        print("Go to the land of the dead. ")