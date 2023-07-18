num = int(input("Enter a five-digit integer: "))

for i in range(5):
    digit = num // 10 ** 4
    print(digit)
    num %= 10 ** 4