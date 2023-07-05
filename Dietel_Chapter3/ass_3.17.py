for i in range(1, 11):
    for j in range(i):
        print('*', end='')
    print()

for i in range(10, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

for i in range(10, 0, -1):
    for j in range(10 - i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()

for i in range(1, 11):
    for j in range(10 - i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()