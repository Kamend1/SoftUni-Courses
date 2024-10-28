from django.urls import path, include
from FurryFunniesApp.authors import views

urlpatterns = [
    path('create/', views.AuthorCreate.as_view(), name='create-author'),
    path('details', views.AuthorDetails.as_view(), name='details-author'),
    path('edit/', views.AuthorUpdate.as_view(), name='edit-author'),
    path('delete/', views.AuthorDelete.as_view(), name='delete-author'),
]