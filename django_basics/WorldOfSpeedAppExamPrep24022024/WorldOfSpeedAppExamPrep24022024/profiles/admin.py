from django.contrib import admin

from WorldOfSpeedAppExamPrep24022024.profiles.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'age', 'first_name', 'last_name']