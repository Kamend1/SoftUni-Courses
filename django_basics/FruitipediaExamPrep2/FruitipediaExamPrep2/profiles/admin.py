from django.contrib import admin

from FruitipediaExamPrep2.profiles.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'age']