from django.contrib import admin

from FurryFunniesApp.authors.models import Author


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'passcode', 'pets_number', 'info', 'image_url',]
