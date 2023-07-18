terms = int(input("Enter the number of terms to approximate π: "))

approximation = 0
sign = 1

print("Approximations:")
for i in range(1, terms + 1):
    term = 4 / (2 * i - 1)
    approximation += sign * term
    sign *= -1

    print(f"Term {i}: {approximation}")

print("\nNumber of terms needed to approximate π:")
target_values = [3.14, 3.141, 3.1415, 3.14159]
for target in target_values:
    approximation = 0
    sign = 1
    num_terms = 0

    while abs(approximation - target) >= 0.00001:
        num_terms += 1
        term = 4 / (2 * num_terms - 1)
        approximation += sign * term
        sign *= -1

    print(f"π ≈ {target}: {num_terms} terms")
