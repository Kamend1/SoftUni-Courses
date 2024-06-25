import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


# Import your models here
from main_app.models import Student


# # Run and print your queries
# Import your models
from main_app.models import Student

def add_students():
    # Adding students using the create method
    if not Student.objects.filter(email="john.doe@university.com").exists():
        Student.objects.create(
            student_id="FC5204",
            first_name="John",
            last_name="Doe",
            birth_date="1995-05-15",
            email="john.doe@university.com"
        )

    if not Student.objects.filter(email="jane.smith@university.com").exists():
        Student.objects.create(
            student_id="FE0054",
            first_name="Jane",
            last_name="Smith",
            email="jane.smith@university.com"
        )

    # Adding students using the save method
    if not Student.objects.filter(email="alice.johnson@university.com").exists():
        alice = Student(
            student_id="FH2014",
            first_name="Alice",
            last_name="Johnson",
            birth_date="1998-02-10",
            email="alice.johnson@university.com"
        )
        alice.save()

    if not Student.objects.filter(email="bob.wilson@university.com").exists():
        bob = Student(
            student_id="FH2015",
            first_name="Bob",
            last_name="Wilson",
            birth_date="1996-11-25",
            email="bob.wilson@university.com"
        )
        bob.save()

def get_students_info():
    students = Student.objects.all()
    result = []

    for student in students:
        result.append(f"Student №{student.student_id}: {student.first_name} {student.last_name}; Email: {student.email}")

    return "\n".join(result)


def update_students_emails():
    students = Student.objects.all()

    for student in students:
        student.email = student.email.replace("university.com", "uni-students.com")

    Student.objects.bulk_update(students, ['email'])


def truncate_students():
    students = Student.objects.all()
    students.delete()

add_students()
print(Student.objects.all())

# print(get_students_info())

# update_students_emails()
# for student in Student.objects.all():
#     print(student.email)

# truncate_students()
# print(Student.objects.all())
# print(f"Number of students: {Student.objects.count()}")
