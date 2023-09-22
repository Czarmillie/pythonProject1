def check_even(number):
    if number % 2 == 0:
        print("True")
    else:
        print("False")


check_even(5)
check_even(6)


def sum1(n):
    total = 0
    for counter in range(1, n+1):
        total += counter
    print(total)

sum1(10)
sum1(20)
sum1(30)