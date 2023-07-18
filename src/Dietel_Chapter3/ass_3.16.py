largest1 = float('-inf')
largest2 = float('-inf')
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))

    if num > largest1:
        largest2 = largest1
        largest1 = num
    elif num > largest2:
        largest2 = num

print("The two largest numbers are:", largest1, "and", largest2)