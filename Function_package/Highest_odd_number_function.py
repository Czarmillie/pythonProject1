
def find_highest_odd_number(numbers_list):
    new_list = []

    for index in numbers_list:
        if index % 2 == 1:
            new_list.append(index)
    highest_number = new_list[0]
    for number in new_list[1:]:
        if number > highest_number:
            highest_number = number

    return highest_number

# Example:
list1 = [19, 23, 3, 4, 5, 6, 7, 899, 99, 10]
print(find_highest_odd_number(list1))