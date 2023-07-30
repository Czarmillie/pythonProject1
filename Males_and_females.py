def count_males_and_females(students_list):
    male_count = 0
    female_count = 0

    for student in students_list:
        if student.lower() == 'male':
            male_count += 1
        elif student.lower() == 'female':
            female_count += 1

    result = [('Male', male_count), ('female', female_count)]
    return result

students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

result_list = count_males_and_females(students)
print(result_list)
