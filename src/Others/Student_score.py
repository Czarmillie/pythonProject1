# print("**************************************************************************************")
# print("Aso Rock Secondary School, Abuja Nigeria")
# print("**************************************************************************************")
#
#
# class Class:
#     pass
#
#
# student_class = Class
# number_of_students = 20
# total = 0
# counter = 1
#
# for counter in range(1, number_of_students):
#     score = int(input(f'Enter score of student {counter}:  '))
#     counter += 1
#     total += score
#
# average = total / counter
# print('''*********************************************************************
#                     Aso Rock Secondary School Abuja, Nigeria
# *********************************************************************''')
# print("Class: SS3")
# print('Number of students in class: ', counter)
# print('Total score: ', total)
# print('Average Score: ', average)
# print('*********************************************************************')
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for row in picture:
    for pixel in row:
        if pixel == 0:
            print(' ', end= '')
        elif pixel == 1:
            print('*', end= '')
    print()