from django.urls import path, include
from WorldOfSpeedAppExamPrep24022024.cars import views

urlpatterns = [
    path('catalogue/', views.CatalogueView.as_view(), name='catalogue'),
    path('create/', views.CarCreateView.as_view(), name='car-create'),
    path('<int:pk>/', include([
        path('details/', views.CarDetailsView.as_view(), name='car-details'),
        path('edit/', views.CarUpdateView.as_view(), name='car-edit'),
        path('delete/', views.CarDeleteView.as_view(), name='car-delete'),
    ]))

]