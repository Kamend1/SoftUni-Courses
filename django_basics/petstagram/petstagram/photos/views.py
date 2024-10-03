from django.shortcuts import render
from petstagram.photos.models import Photo


# Create your views here.
def add_photo(request):
    return render(request, 'photos/photo-add-page.html')


def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments
    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)

    context = {
        'pk': pk,
        'photo': photo,
    }

    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)

    context = {
        'pk': pk,
        'photo': photo,
    }

    return render(request, 'photos/photo-edit-page.html', context)