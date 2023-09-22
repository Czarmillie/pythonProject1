def remove_duplicates(old_array):
    new_array = []
    for index in old_array:
        if index in new_array:
            continue
        else:
            new_array += [index]
    return new_array


num_list = [4, 6, 7, 9, 4, 9, 7, 3, 1, 7, 8, 2, 6, 3, 1]
String_list = ['Daniel', 'O.G Laflare', 'Seyi', 'Grace', 'Tomide', 'Esther', 'O.G Laflare', 'Grace']
print(remove_duplicates(num_list))
print(remove_duplicates(String_list))