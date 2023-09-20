name_student = input()
grade = 0
fail_counter = 0
total_score = 0

while grade < 12:
    input_grade_score = float(input())
    if input_grade_score < 4.00:
        fail_counter += 1
        total_score += input_grade_score
    if fail_counter == 2:
        print(f"{name_student} has been excluded at {int(grade)} grade")
        break

    total_score += input_grade_score
    grade += 1

average_score = total_score / grade
if grade == 12:
    print(f"{name_student} graduated. Average grade: {average_score:.2f}")
