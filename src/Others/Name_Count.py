def count_names_starting_with_s(names_list):
    names_dict = {}

    for name in names_list:
        name = name.capitalize()
        if name[0] == 'S':
            if name in names_dict:
                names_dict[name] += 1
            else:
                names_dict[name] = 1

    return names_dict

names_list = ['Sarah', 'Sam', 'Sophia', 'Steven', 'John', 'Samantha', 'Sophia', 'Asa', 'Ashley', 'Daniel', 'Steven',
              'sophia', 'Samantha', 'Susu']
result = count_names_starting_with_s(names_list)
print(result)