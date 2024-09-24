from petstagram.pets import views
from django.urls import path, include

urlpatterns = [
    path('add/', views.add_pet, name='pet-add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.pet_details, name='pet-details'),
        path('edit/', views.edit_pet, name='pet-edit'),
        path('delete/', views.delete_pet, name='pet-delete'),
    ])),
]
