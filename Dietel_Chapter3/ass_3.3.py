for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
    print()


for _ in range(2):
    for _ in range(7):
        print('@', end='')
    print()