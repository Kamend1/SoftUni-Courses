def softuni_students(*args, **kwargs):
    students = sorted(args, key=lambda x: x[1])
    matched_students = []
    unmatched_students = []
    string_to_print = ""

    for current_student in students:

        if current_student[0] in kwargs:
            matched_students.append(current_student)
        else:
            unmatched_students.append(current_student)

    for student in matched_students:
        current_string = (f"*** A student with the username {student[1]} "
                            f"has successfully finished the course {kwargs.get(student[0])}!\n")
        string_to_print += current_string
    if unmatched_students:
        unmatched_students = sorted(unmatched_students, key=lambda x: x[1])
        string_to_print += f"!!! Invalid course students: {', '.join(student[1] for student in unmatched_students)}"
        return string_to_print
    else:
        return string_to_print


print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))


