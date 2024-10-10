from django.contrib import admin

from MyMusicAppExamPrep1.album.models import Album


# Register your models here.
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['album_name', 'artist', 'genre', 'image', 'price']
    readonly_fields = ['owner']

