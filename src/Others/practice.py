# match language:
#     case "java":
#         print(f"You are a hardcore programmer")
#     case "javascript":
#         print(f"You are too much")
#     case "Python":
#         print(f"You are amazing")
#     case _:
#         print("You are a learner")


# numbers = [10, 20, 30, 40, 50]
# total = 0
# for num in numbers:
#     total += num
# print("The sum is:", total)


# numbers = [10, 20, 30, 40, 50]
# sum = 0
# for list in [0: :2]
# print(result)


# numbers = [10, 20, 30, 40, 50]
# square_of = [num ** 2 for num in numbers]
# for square in square_of:
#     print(square)


# numbers = [10, 20, 30, 40, 50]
# highest_number = numbers[0]
# lowest_number = numbers[0]
# square_of = [num ** 2 for num in numbers]
# for index,value in enumerate(numbers):
#     print("value",value,"lowest number",lowest_number)
#     if lowest_number > value:
#         lowest_number = value
#     if highest_number < value:
#         highest_number = value
# print(lowest_number ** 2)
# print(highest_number ** 2)

# numbers = [8, 2, 5, 6, 1, 3, 9, 4, 7]

# for num in range(len(numbers)):
#     for num2 in range(len(numbers)):
#         if numbers[num2] > numbers[num]:
#             numbers[num2], numbers[num] = numbers[num], numbers[num2]
# print(numbers)

#
# numbers = [8, 2, 5, 6, 1, 3, 9, 4, 7]
# print(numbers[::-1])


# numbers = [8, 2, 5, 6, 1, 3, 9, 4, 7]
# for i in range(0, 10, -1):
#     print(numbers)

#
# t1 = (1, 3, 2)
# x = t1[0] + t1[2]
def test2(number):
    if number % 2 == 0:
        return number

x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(test2, x1)))