from django.urls import path, include
from MyMusicAppExamPrep1.album import views

urlpatterns = [
    path('add/', views.album_add, name='album-add'),
    path('<int:id>/', include([
        path('', views.album_details, name='album-details'),
        path('edit/', views.album_edit, name='album_edit'),
        path('delete/', views.album_delete, name='album-delete'),]
    )),
]
