def check_duplicates(strings):
    string_counts = {}

    for string in strings:
        if len(string) in len(set(string_counts)):
            return string
        string_counts[string] = 1
    else:
        return "No duplicates"


strings_list = ["apple", "banana", "banana", "apple", "grape"]
result = check_duplicates(strings_list)
print(result)