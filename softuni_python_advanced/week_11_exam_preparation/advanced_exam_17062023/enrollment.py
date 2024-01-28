def gather_credits(credits_needed, *course_credits,):
    enrolled_courses = []
    credits_taken = 0
    for course in course_credits:
        course_name, course_credits = course
        if credits_needed > 0 and course_name not in enrolled_courses:
            credits_taken += course_credits
            credits_needed -= course_credits
            enrolled_courses.append(course_name)
        elif credits_needed <= 0:
            break

    if credits_needed <= 0:
        return (f"Enrollment finished! Maximum credits: {credits_taken}.\n"
                f"Courses: {', '.join(sorted(enrolled_courses))}")
    else:
        return f"You need to enroll in more courses! You have to gather {credits_needed} credits more."

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))


