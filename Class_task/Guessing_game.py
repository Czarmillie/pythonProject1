import random

number = random.randint(1, 11)
counter = 0
while counter < 10:
    number_guessed = int(input('Enter Number: '))
    if number_guessed < 1 or number_guessed >= 4:
        print("Too low, try again!!!")
    elif number_guessed >= 6 or number_guessed <= 10:
        print("Too high, try again")
    elif number_guessed == 5:
        print('Guessed correctly. ')
    else:
        break
    counter += 1

if counter == 5:
    print("THANK YOU!!! Tries exhausted")


