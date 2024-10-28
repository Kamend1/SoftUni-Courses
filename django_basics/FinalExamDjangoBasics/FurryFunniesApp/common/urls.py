from django.urls import path
from FurryFunniesApp.common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]