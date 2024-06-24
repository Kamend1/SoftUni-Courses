from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudenrAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'birth_date', 'email')