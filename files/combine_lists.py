def combine_lists(list1, list2):
    combined_list = []
    length = min(len(list1), len(list2))

    for i in range(length):
        combined_list.append(list1[i])
        combined_list.append(list2[i])

    combined_list.extend(list1[length:])
    combined_list.extend(list2[length:])

    return combined_list