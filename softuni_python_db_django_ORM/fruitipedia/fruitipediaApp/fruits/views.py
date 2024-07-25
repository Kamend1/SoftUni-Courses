from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    return render(request, 'common/dashboard.html')


def create_fruit(request):
    return render(request, 'fruits/create-fruit.html')


def details_fruit(request):
    return render(request, 'fruits/details-fruit.html')


def edit_fruit(request):
    return render(request, 'fruits/edit-fruit.html')


def delete_fruit(request):
    return render(request, 'fruits/delete-fruit.html')


def create_category(request):
    return render(request, 'categories/create-category.html')
