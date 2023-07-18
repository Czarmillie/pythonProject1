first_name = (input("What is your first name: "))
last_name = (input("What is your last name: "))
age = int(input("What is your age: "))
if first_name == "":
    print('First Name cannot be empty')
if last_name == "":
    print('Last Name cannot be empty')
if age < 0:
    print('Age cannot be negative')
elif age <= 65:
    print('Your name is', first_name, last_name, 'and your age is', age, 'You are underage')
else:
    print('Your name is', first_name, last_name, 'and your age is', age, 'You are an old citizen. ')