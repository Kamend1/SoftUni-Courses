from petstagram.pets import views
from django.urls import path, include

urlpatterns = [
    path('add/', views.AddPetView.as_view(), name='pet-add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.PetDetailsView.as_view(), name='pet-details'),
        path('edit/', views.EditPetView.as_view(), name='pet-edit'),
        path('delete/', views.DeletePetView.as_view(), name='pet-delete'),
    ])),
]
