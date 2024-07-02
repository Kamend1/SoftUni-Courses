from datetime import date

from django.db import models


# Create your models here.
class Lecturer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    lecturer = models.ForeignKey(to=Lecturer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"


class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    subjects = models.ManyToManyField(to='Subject', through='StudentEnrollment')


class GradeChoices(models.TextChoices):
    A = "A", "A"
    B = "B", "B"
    C = "C", "C"
    D = "D", "D"
    F = "F", "F"


class StudentEnrollment(models.Model):
    student = models.ForeignKey(to='Student', on_delete=models.CASCADE)
    subject = models.ForeignKey(to='Subject', on_delete=models.CASCADE)
    enrollment_date = models.DateField(default=date.today)
    grade = models.CharField(max_length=1, choices=GradeChoices.choices, blank=True, null=True)


class LecturerProfile(models.Model):
    lecturer = models.OneToOneField(Lecturer, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    office_location = models.CharField(max_length=100, blank=True, null=True)
