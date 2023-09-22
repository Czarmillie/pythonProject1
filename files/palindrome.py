def is_palindrome(input_string):
    input_string = ''.join(c for c in input_string if c.isalnum()).lower()

    char_array = list(input_string)

    return char_array == char_array[::-1]