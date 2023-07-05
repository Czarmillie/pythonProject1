counter = 0
failures = 0

while True:
    user_input = input("Enter a value (1 or 2): ")
    counter += 1

    if user_input == '1' or user_input == '2':
        break
    else:
        failures += 1

print("Number of passes:", counter - failures)
print("Number of failures:", failures)