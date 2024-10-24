from django.urls import path, include
from FruitipediaExamPrep2.fruits import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('create/', views.FruitCreate.as_view(), name='create-fruit'),
    path('<int:pk>/', include([
        path('details/', views.FruitDetails.as_view(), name='details-fruit'),
        path('delete/', views.FruitDelete.as_view(), name='delete-fruit'),
        path('edit/', views.FruitEdit.as_view(), name='edit-fruit'),
    ]))
]