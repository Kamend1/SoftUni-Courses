from django.contrib import admin

from FurryFunniesApp.posts.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_url', 'content', 'updated_at', 'author',]
