sum = 0
product = 1
smallest = None
largest = None

for i in range(4):
    num = int(input(f"Enter integer {i+1}: "))

    sum += num
    product *= num

    # Determine smallest and largest numbers
    if smallest is None or num < smallest:
        smallest = num
    if largest is None or num > largest:
        largest = num

average = sum / 4

print(f"Sum: {sum}")
print(f"Average: {average}")
print(f"Product: {product}")
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")