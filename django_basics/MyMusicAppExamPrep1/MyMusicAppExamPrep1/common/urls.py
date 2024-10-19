from django.urls import path
from MyMusicAppExamPrep1.common import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page')
]