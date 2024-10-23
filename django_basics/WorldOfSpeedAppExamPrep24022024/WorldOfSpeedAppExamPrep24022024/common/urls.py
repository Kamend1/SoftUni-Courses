from django.urls import path
from WorldOfSpeedAppExamPrep24022024.common import views

urlpatterns = [
    path('', views.index, name='index'),
]
