def split_list_every_third(lst):
    result = []
    for i in range(3):
        sublist = lst[i::3]
        result.append(sublist)
    return result

sample_input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
result = split_list_every_third(sample_input)
print(result)
