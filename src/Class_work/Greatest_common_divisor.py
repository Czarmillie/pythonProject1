def gcd(a, b):
    while b:
        a, b = b, a % 2
    return a

num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))

result = gcd(num1, num2)
print("The greatest common divisor of", num1, "and", num2, "is", result)
