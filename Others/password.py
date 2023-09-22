password = input('Enter your Password: ')
while len(password) < 8:
    password = input('Enter your Password: ')
if len(password) >= 8:
    print(f'Your password is secure, The length is: {len(password)} ')