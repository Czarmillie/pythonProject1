def colors():
    lists = []
    for elements in list1:
        if elements in list2 != elements in list1:
            lists.append(elements)
            return lists

list1 = (["White", "Black", "Red"])
list2 = (["Red", "Green"])
print(colors())