def count_males_and_females(students_list):
    male_count = 0
    female_count = 0

    for student in students_list:
        if student.lower() == 'male':
            male_count += 1
        elif student.lower() == 'female':
            female_count += 1

    result = [('male', male_count), ('female', female_count)]
    return result

students = ['male', 'female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male', 'female', 'male',
            'female']

result_list = count_males_and_females(students)
print(result_list)