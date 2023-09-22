num = int(input("Enter a five-digit integer: "))

for _ in range(5):
    digit = num % 10
    print(digit)
    num //= 10


initial_amount = 1000
interest_rate = 0.05

amount = initial_amount

for year in range(1, 31):
    amount += amount * interest_rate
    print(f"Year {year}: {amount:.2f}")