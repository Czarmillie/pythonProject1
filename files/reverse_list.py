def reverse_list(x):
    for num in range(len(numbers)):
        for num2 in range(len(numbers)):
            if numbers[num2] <= numbers[num]:
                numbers[num2], numbers[num] = numbers[num], numbers[num2]
    return x
    print(reverse_list(numbers))

numbers = [8, 2, 5, 6, 1, 3, 9, 4, 7]
print(numbers[::-1])