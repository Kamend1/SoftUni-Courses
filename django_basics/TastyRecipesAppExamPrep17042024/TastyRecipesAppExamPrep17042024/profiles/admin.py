from django.contrib import admin
from TastyRecipesAppExamPrep17042024.profiles.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'first_name', 'last_name', 'chef']
