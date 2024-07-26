from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from fruitipediaApp.fruits.models import Fruit
from fruitipediaApp.fruits.forms import CategoryAddForm, FruitAddForm, FruitEditForm, FruitDeleteForm


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):

    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits
    }

    return render(request, 'common/dashboard.html', context)


def create_fruit(request):
    if request.method == 'POST':
        form = FruitAddForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = FruitAddForm()

    context = {
        'form': form,
    }

    return render(request, 'fruits/create-fruit.html', context)


def details_fruit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()

    context = {
        'fruit': fruit,
    }

    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()

    if request.method == 'POST':
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
        return redirect('dashboard')
    else:
        form = FruitEditForm(instance=fruit)

    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruits/edit-fruit.html', context)


def delete_fruit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()

    if request.method == 'POST':
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            fruit.delete()
        return redirect('dashboard')
    else:
        form = FruitDeleteForm(instance=fruit)

    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruits/delete-fruit.html', context)


def create_category(request):
    if request.method == 'POST':
        form = CategoryAddForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = CategoryAddForm()

    context = {
        'form': form,
    }

    return render(request, 'categories/create-category.html', context)
