def intersection():
    intersected_list = []
    for elements in list1:
        if elements in list2:
            intersected_list.append(elements)
    return intersected_list


list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [42, 30, 80, 65, 68, 88, 95]
print(intersection())