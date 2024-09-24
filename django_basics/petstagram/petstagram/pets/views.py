from django.shortcuts import render


# Create your views here.
def add_pet(request):
    return render(request, 'pets/pet-add-page.html')


def pet_details(request, username, pet_slug):
    context = {
        'username': username,
        'pet_slug': pet_slug,
    }

    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request, username, pet_slug):
    context = {
        'username': username,
        'pet_slug': pet_slug,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, username, pet_slug):
    context = {
        'username': username,
        'pet_slug': pet_slug,
    }

    return render(request, 'pets/pet-delete-page.html', context)
