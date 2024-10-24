from django.urls import path
from FruitipediaExamPrep2.common import views

urlpatterns = [
    path('', views.index, name='index'),
]