for i in range(1, 6):
    # Pattern 1
    for j in range(i):
        print('*', end='')
    print('   ', end='')

    for j in range(5, i - 1, -1):
        print('*', end='')
    print('   ', end='')

    for j in range(5 - i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print('   ', end='')

    for j in range(i - 1):
        print(' ', end='')
    for j in range(5 - i + 1):
        print('*', end='')

    print()
