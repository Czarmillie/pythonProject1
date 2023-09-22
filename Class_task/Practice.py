# from Class_task.DogException import DogException
#
#
# def number_of_legs_setter(args):
#     pass
#
#
# class Animal:
#     def __int__(self):
#         self.number_of_nose = 1
#
#     @property
#     def number_of_legs(self):
#         return self.number_of_legs
#
#
#     @number_of_legs_setter
#     def number_of_legs(self, value):
#         if value != 4:
#             raise DogException("Invalid number of legs. ")
#     def eat(self):
#         print("Eating")
#
# class dog(Animal):
#     def __int__(self):
#         self.number_of_legs = 4
#         super().__int__()
#
#     def walk(self):
#         print(f"Walking with {self.number_of_legs}")
#
# class fish(Animal):
#     def swim(self):
#         print("Swimming")
#
# f1 = fish()
# f1.number_of_nose
# d1 = dog()

# def big_list(num: int):
#     double = []
#     for i in range(num):
#         double.append(i * 2)
#     return double
#
# def generator_func(n):
#     for x in range(n):
#         yield x
#
# # print(big_list(10000))
#
# a = generator_func(1000)
# print(next(a))
# next(a)
# print(next(a))

# import tkinter as tk
#
# window = tk.Tk()
# window.title("Hello, Tkinter!")
#
# label = tk.Label(window, text="Hello, Tkinter!")
# label.pack()
#
# window.mainloop()


# from translate import Translator
#
# text = "Ace clan are mad people"
#
# translator = Translator(to_lang='lat')
# translation = translator.translate(text)
# print(translation)


# from googletrans import Translator
#
#
# def translate_text(text, target_language):
#     translator = Translator()
#     translated_text = translator.translate(text, dest=target_language)
#
#     return translated_text.text
#
#
# text_to_translate = "have you eaten?"
# target_language = "yo"
# translated_text = translate_text(text_to_translate, target_language)
#
# print(f"Original Text: {text_to_translate}")
# print(f"Translated Text: {translated_text}")


# def find_non_duplicate(numbers):
#     number_count = {}
#     for num in numbers:
#         number_count[num] = number_count.get(num, 0) + 1
#
#     non_duplicates = [num for num, count in number_count.items() if count == 1]
#     return non_duplicates
#
# print(*find_non_duplicate([2, 2, 1]))
# print(*find_non_duplicate([4, 3, 2, 2, 3, 3]))
# print(*find_non_duplicate([1]))


# from collections import Counter
# def find_non_duplicate(numbers):
#     counter = Counter(numbers)
#     return [num for num, count in counter.items() if count == 1]
#
# print(*find_non_duplicate([4, 3, 2, 2, 3, 3]))
# # print(*find_non_duplicate([2, 2, 1]))
# # print(*find_non_duplicate([1]))


def find_non_duplicate(numbers):
    number_count = {}
    non_duplicates = []

    for num in numbers:
        if num in number_count:
            number_count[num] += 1
        else:
            number_count[num] = 1

    for num, count in number_count.items():
        if count == 1:
            non_duplicates.append(num)

    return non_duplicates

print(*find_non_duplicate([2, 2, 1]))
print(*find_non_duplicate([4, 3, 2, 2, 3, 3]))
print(*find_non_duplicate([1]))

