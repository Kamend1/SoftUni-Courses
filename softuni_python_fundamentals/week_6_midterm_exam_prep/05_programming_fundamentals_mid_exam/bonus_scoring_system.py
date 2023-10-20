from math import ceil

number_students = int(input())
number_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
best_student_attendance = 0

for i in range(number_students):
    current_student_attendance = int(input())
    current_student_bonus = ((current_student_attendance / number_lectures) * (5 + additional_bonus))
    if current_student_attendance > best_student_attendance:
        best_student_attendance = current_student_attendance
        max_bonus = ((best_student_attendance / number_lectures) * (5 + additional_bonus))
print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {best_student_attendance} lectures.")
