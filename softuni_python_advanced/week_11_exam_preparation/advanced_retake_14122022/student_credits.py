def students_credits(*credits):
    credits_earned = 0
    courses_passed = {}

    for course in credits:
        course, credits, max_score, diyan_score = course.split('-')
        current_credits = (int(diyan_score) / int(max_score)) * int(credits)
        if course not in courses_passed:
            courses_passed[course] = 0
        courses_passed[course] = current_credits
        credits_earned += current_credits

    sorted_passed_courses = dict(sorted(courses_passed.items(), key=lambda x: -x[1]))

    if credits_earned >= 240:
        string = ''
        string += f"Diyan gets a diploma with {credits_earned:.1f} credits."
        for k, v in sorted_passed_courses.items():
            string += "\n" + f"{k} - {v:.1f}"
        return string

    else:
        string = ''
        string += f"Diyan needs {(240 - credits_earned):.1f} credits more for a diploma."
        for k, v in sorted_passed_courses.items():
            string += "\n" + f"{k} - {v:.1f}"
        return string


# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )

# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )
#
# print(
#     students_credits(
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Java Development-10-300-150"
#     )
# )
