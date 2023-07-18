purchase_price = float(input("Enter the purchase price (in dollars): "))
change_due = 100 - int(purchase_price * 100)

quarters = change_due // 25
change_due %= 25

dimes = change_due // 10
change_due %= 10

nickels = change_due // 5
change_due %= 5

pennies = change_due

print("Your change is:")
print(quarters, "quarters")
print(dimes, "dimes")
print(nickels, "nickels")
print(pennies, "pennies")
