from django.urls import path
from TastyRecipesAppExamPrep17042024.common import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
]