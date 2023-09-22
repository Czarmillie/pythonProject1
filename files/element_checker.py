numbers = [10, 20, 30, 40, 50]
highest_number = numbers[0]
square_of = [num ** 2 for num in numbers]
for index,value in enumerate(numbers):
    print("value", value, "highest number")
    if highest_number < value:
        highest_number = value