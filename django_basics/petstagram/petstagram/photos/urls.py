from petstagram.photos import views
from django.urls import path, include

urlpatterns = [
    path('add/', views.add_photo, name='photo-add'),
    path('<int:pk>/', include([
        path('', views.photo_details, name='photo-details'),
        path('edit/', views.edit_photo, name='photo-edit'),
        path('delete/', views.delete_photo, name='photo-delete'),
    ])),
]