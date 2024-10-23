from django.urls import path
from WorldOfSpeedAppExamPrep24022024.profiles import views

urlpatterns = [
    path('create/', views.ProfileCreateView.as_view(), name='profile-create'),
    path('details/', views.ProfileDetailsView.as_view(), name='profile-details'),
    path('delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
    path('edit/', views.ProfileUpdateView.as_view(), name='profile-edit'),
]