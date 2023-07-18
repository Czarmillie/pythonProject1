print("***************************************************************************************")
print("Aso Rock Secondary School, Abuja Nigeria")
print("***************************************************************************************")

student_class = 1
total = 0
counter = 1

while True:
    score = int(input(f'Enter score of student {counter} or -25 to end :  '))

    if score == -25:
        break

    counter += 1
    total += score
if total > 0:
    average = total / counter

print('''*********************************************************************
                    Aso Rock Secondary School Abuja, Nigeria
*********************************************************************''')
print("Class: SS3")
print('Number of students in class: ', counter)
print('Total score: ', total)
print('Average Score: ', average)
print('*********************************************************************')