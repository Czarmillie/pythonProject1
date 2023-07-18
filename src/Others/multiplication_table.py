def multiplication_table(number):
    for j in range(1, 13):
        for i in range(1, number + 1):
            print(f"{i:>5} x {j:>4} = {i * j}", end='\t\t')
        print()


num = int(input("Enter a number between 1 and 1000: "))
if num < 1 or num > 1000:
    print("Invalid input. Please enter a number between 1 and 1000.")
else:
    multiplication_table(num)