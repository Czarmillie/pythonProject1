def find_intersection(list1, list2):
    intersection = tuple(set(list1) & set(list2))
    return intersection

list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [42, 30, 80, 65, 68, 88, 95]

intersection = find_intersection(list1, list2)
print(intersection)
