number_people_jury = int(input())
count_presentations = 0
sum_average_grades = 0

name_presentation_or_command = input()

while name_presentation_or_command != "Finish":
    count_presentations += 1
    current_presentation_grade = 0
    for presentation_grade in range(number_people_jury):
        current_member_grade = float(input())
        current_presentation_grade += current_member_grade
    current_presentation_average = current_presentation_grade / number_people_jury
    print(f"{name_presentation_or_command} - {current_presentation_average:.2f}.")
    sum_average_grades += current_presentation_average

    name_presentation_or_command = input()

average_student_grade = sum_average_grades / count_presentations
print(f"Student's final assessment is {average_student_grade:.2f}.")
