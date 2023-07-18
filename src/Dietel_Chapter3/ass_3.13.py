num = int(input("Enter a nonnegative integer: "))
if num < 0:
    print("Invalid input. Please enter a nonnegative integer.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is: {factorial}")