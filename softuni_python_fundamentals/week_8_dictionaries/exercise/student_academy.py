student_grades = {}

number_inputs = int(input())

for i in range(number_inputs):
    name = input()
    grade = float(input())
    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

for student, grades in student_grades.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
