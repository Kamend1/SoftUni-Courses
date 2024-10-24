from django.urls import path
from FruitipediaExamPrep2.profiles import views

urlpatterns = [
    path('create/', views.ProfileCreate.as_view(), name='create-profile'),
    path('details/', views.ProfileDetails.as_view(), name='details-profile'),
    path('edit/', views.ProfileEdit.as_view(), name='edit-profile'),
    path('delete/', views.ProfileDelete.as_view(), name='delete-profile'),
]
