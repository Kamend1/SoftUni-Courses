number_students = int(input())
top_students = 0
very_good_students = 0
average_students = 0
fail_students = 0
total_exam_grade = 0

for i in range(number_students):
    exam_grade = float(input())
    total_exam_grade += exam_grade
    if exam_grade >= 5.00:
        top_students += 1
    elif exam_grade >= 4.00:
        very_good_students += 1
    elif exam_grade >= 3.00:
        average_students += 1
    else:
        fail_students += 1

percent_top_students = top_students * 100 / number_students
percent_very_good = very_good_students * 100 / number_students
percent_average = average_students * 100 / number_students
percent_fail = fail_students * 100 / number_students
average_exam_grade = total_exam_grade / number_students

print(f"Top students: {percent_top_students:.2f}%")
print(f"Between 4.00 and 4.99: {percent_very_good:.2f}%")
print(f"Between 3.00 and 3.99: {percent_average:.2f}%")
print(f"Fail: {percent_fail:.2f}%")
print(f"Average: {average_exam_grade:.2f}")
