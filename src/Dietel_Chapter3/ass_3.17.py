for counter in range(10):
    for counter1 in range(counter + 1):
        print('*', end=' ')
    for counter1 in range(10 - counter):
        print(' ', end=' ')
    for counter1 in range(10 - counter):
        print('*', end=' ')
    for counter1 in range(counter + 1):
        print(' ', end=' ')
    for counter1 in range(counter + 1):
        print(' ', end=' ')
    for counter1 in range(10 - counter):
        print('*', end=' ')
    for counter1 in range(10 - counter):
        print(' ', end=' ')
    for counter1 in range(counter + 1):
        print('*', end=' ')
    print()