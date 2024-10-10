from django.contrib import admin
from MyMusicAppExamPrep1.profile.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'age']
