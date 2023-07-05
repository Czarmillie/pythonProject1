# first_name = (input("What is your first name: "))
# last_name = (input("What is your last name: "))
# age = int(input("What is your age: "))
# if first_name == "":
#     print('First Name cannot be empty')
# if last_name == "":
#     print('Last Name cannot be empty')
# if age < 0:
#     print('Age cannot be negative')
# elif age <= 65:
#     print('Your name is', first_name, last_name, 'and your age is', age, 'You are underage')
# else:
#     print('Your name is', first_name, last_name, 'and your age is', age, 'You are an old citizen. ')


# language = input("Enter your preferred language: ")
# if language  == "java":
#     print(f"you are a hardcore programmer")
# elif language == "javascript":
#     print(f"You are too much")
# elif language == "python":
#     print("You are a learner")


# match language:
#     case "java":
#         print(f"You are a hardcore programmer")
#     case "javascript":
#         print(f"You are too much")
#     case "Python":
#         print(f"You are amazing")
#     case _:
#         print("You are a learner")


# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print('True')
# else:
#     print('false')


# number = int(input("Enter a number: "))
# print(number % 2 == 0)


# def check_even():
#     number = int(input("Enter a number: "))
#     if number % 2 == 0:
#         print("True")
#     else:
#         print("False")
#
#
# check_even()


# def check_even(number):
#     if number % 2 == 0:
#         print("True")
#     else:
#         print("False")
#
#
# check_even(5)
# check_even(6)


# def sum1(n):
#     total = 0
#     for counter in range(1, n+1):
#         total += counter
#     print(total)
#
# sum1(10)
# sum1(20)
# sum1(30)


def find_maximum_number(a, b, c, d):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    if d > maximum:
        maximum = d
    return maximum
num1 = 100
num2 = 250
num3 = 50
num4 = 150
greatest_number = find_maximum_number(num1, num2, num3, num4)
print("The greatest number is:", greatest_number)
def find_minimum_number(a, b, c, d):
    minimum = a
    if b < minimum:
        minimum = b
    if c < minimum:
        minimum = c
    if d < minimum:
        minimum = d
    return minimum
lowest_number = find_minimum_number(num1, num2, num3, num4)
print("The lowest number is:", lowest_number)