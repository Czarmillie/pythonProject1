def find_maximum_number(a, b, c, d):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    if d > maximum:
        maximum = d
    return maximum
num1 = 100
num2 = 250
num3 = 50
num4 = 150
greatest_number = find_maximum_number(num1, num2, num3, num4)
print("The greatest number is:", greatest_number)
def find_minimum_number(a, b, c, d):
    minimum = a
    if b < minimum:
        minimum = b
    if c < minimum:
        minimum = c
    if d < minimum:
        minimum = d
    return minimum
lowest_number = find_minimum_number(num1, num2, num3, num4)
print("The lowest number is:", lowest_number)