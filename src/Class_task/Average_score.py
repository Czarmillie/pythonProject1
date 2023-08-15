print("**************************************************************************************")
print("Aso Rock Secondary School, Abuja Nigeria")
print("**************************************************************************************")

class_name = "SSS 3"
num_students = 20
total_score = 0

for counter in range(1, num_students + 1):
    while True:
        try:
            score = float(input(f"Enter the score for Student {counter}: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    total_score += score

average_score = total_score / num_students

print("**************************************************************************************")
print(f"Class: {class_name}")
print(f"Number of Students in Class: {num_students}")
print(f"Total Score: {total_score}")
print("Average Score: {:.2f}".format(average_score))
print("**************************************************************************************")
