import math

terms = 10
approximation = 1
factorial = 1

print("Approximations:")
for i in range(1, terms + 1):
    factorial *= i
    term = 1 / factorial
    approximation += term

    print(f"Term {i}: {approximation}")

print(f"\nEstimated value of e using {terms} terms: {approximation}")
print(f"Actual value of e: {math.e}")
