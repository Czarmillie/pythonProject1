import random

number = random.randint(1, 10)
counter = 0

while counter < 10:
    number_guessed = int(input('Enter Number: '))
    if number_guessed == number:
        print("CONGRATULATIONS You are a genius!!!")
        break
    else:
        print('WRONG!!! Please try again')
    counter += 1

if counter == 10:
    print("THANK YOU!!! Tries exhausted")


