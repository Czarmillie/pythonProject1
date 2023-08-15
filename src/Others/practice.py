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


# def test2(number):
#     if number % 2 == 0:
#         return number
#
# x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(test2, x1)))


# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print([index ** 2 for index in list1])
#
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print([i for i in list2 if i % 2 == 0])
# print([index ** 2 for index in list2 if index % 2 == 0])

#
# def is_palindrome(string):
#     return string == string[::-1]
# print(is_palindrome("mom"))

# def check_duplicates(strings):
#     # Create an empty dictionary to store the counts of each string
#     string_counts = {}
#
#     # Iterate through each string in the list
#     for string in strings:
#         # If the string is already in the dictionary, it's a duplicate
#         if string in string_counts:
#             return string  # Return the duplicate found
#
#         # Otherwise, add the string to the dictionary with a count of 1
#         string_counts[string] = 1
#
#     # If no duplicates were found, return "No duplicates"
#     return "No duplicates"

# import re


# def email_validator(emails):
#     valid_emails = []
#
#     for email in emails:
#         # Check for @ symbol
#         if email.count('@') != 1 or email.startswith('@'):
#             continue
#
#         # Split email into name and domain
#         name, domain = email.split('@')
#
#         # Check for valid domain ending
#         if not re.match(r'\.[a-zA-Z]{2,}$', domain):
#             continue
#
#         valid_emails.append(email)
#
#     return valid_emails
#
#
# # Test the function
# emails_to_check = ["user@example.com", "invalid@.com", "@invalid.com", "user@example", "user@domain.abc"]
# valid_emails = email_validator(emails_to_check)
# print(valid_emails)