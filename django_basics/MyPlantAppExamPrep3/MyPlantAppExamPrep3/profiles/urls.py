from django.urls import path
from MyPlantAppExamPrep3.profiles import views

urlpatterns = [
    path('create/', views.ProfileCreateView.as_view(), name='create-profile'),
    path('edit/', views.ProfileUpdateView.as_view(), name='edit-profile'),
    path('delete/', views.ProfileDeleteView.as_view(), name='delete-profile'),
    path('details/', views.ProfileDetailsView.as_view(), name='details-profile')
]
