from django.urls import path
from MyPlantAppExamPrep3.plants import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('catalogue/', views.CatalogueView.as_view(), name='catalogue'),
    path('create/', views.PlantCreate.as_view(), name='create-plant'),
    path('delete/<int:pk>/', views.PlantDelete.as_view(), name='delete-plant'),
    path('edit/<int:pk>/', views.PlantUpdate.as_view(), name='edit-plant'),
    path('details/<int:pk>/', views.PlantDetails.as_view(), name='details-plant'),
]

