from django.urls import path, include
from FurryFunniesApp.posts import views

urlpatterns = [
    path('create/', views.CreatePost.as_view(), name='create-post'),
    path('<int:pk>/', include([
        path('edit/', views.EditPost.as_view(), name='edit-post'),
        path('delete/', views.DeletePost.as_view(), name='delete-post'),
        path('details/', views.DetailsPost.as_view(), name='details-post'),
    ]))
]
