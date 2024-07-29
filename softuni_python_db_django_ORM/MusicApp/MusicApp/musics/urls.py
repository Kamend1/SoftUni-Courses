from django.urls import path, include

from MusicApp.musics import views

urlpatterns = [
    path('', views.index, name='index'),
    path('albums/', include([
        path('create/', views.create_album, name='create_album'),
        path('edit/<int:id>/', views.edit_album, name='edit_album'),
        path('delete/<int:id>/', views.delete_album, name='delete_album'),
        path('details/<int:id>/', views.album_details, name='details_album'),
    ])),
    path('songs/', include([
        path('create/', views.create_song, name='create_song'),
        path('play-song/<int:pk>', views.play_song, name="play song"),
        path('serve-song/<int:pk>', views.serve_song, name='serve song'),
    ]))
]