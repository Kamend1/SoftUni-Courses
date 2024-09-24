from petstagram.common import views
from django.urls import path, include

urlpatterns = [
    path('', views.home_page, name='home-page'),
]