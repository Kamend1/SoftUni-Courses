number_students = int(input())
total_score = 0
top_students = 0
good_students = 0
average_students = 0
fail_students = 0

for _ in range(number_students):
    grade = float(input())
    total_score += grade
    if grade < 3:
        fail_students += 1
    elif grade < 4:
        average_students += 1
    elif grade < 5:
        good_students += 1
    elif grade >= 5:
        top_students += 1

percent_top_students = top_students * 100 / number_students
percent_good_students = good_students * 100 / number_students
percent_average_students = average_students * 100 / number_students
percent_fail_students = fail_students * 100 / number_students
average_grade = total_score / number_students

print(f"Top students: {percent_top_students:.2f}%")
print(f"Between 4.00 and 4.99: {percent_good_students:.2f}%")
print(f"Between 3.00 and 3.99: {percent_average_students:.2f}%")
print(f"Fail: {percent_fail_students:.2f}%")
print(f"Average: {average_grade:.2f}")
