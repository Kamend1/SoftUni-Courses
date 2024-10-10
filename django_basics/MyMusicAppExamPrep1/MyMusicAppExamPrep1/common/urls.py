from django.urls import path
from MyMusicAppExamPrep1.common import views


urlpatterns = [
    path('', views.home_page, name='home-page')
]