from django.shortcuts import render, redirect
from petstagram.photos.models import Photo
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from petstagram.common.forms import CommentForm


# Create your views here.
def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home-page')

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)


def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    comment_form = CommentForm()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)

    if request.method == 'GET':
        form = PhotoEditForm(instance=photo, initial=photo.__dict__)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'pk': pk,
        'photo': photo,
        'form': form
    }

    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)

    if request.method == 'POST':
        photo.delete()
        return redirect('home-page')
    else:
        form = PhotoDeleteForm(instance=photo, initial=photo.__dict__)

    context = {
        'pk': pk,
        'photo': photo,
        'form': form,
    }

    return render(request, 'photos/photo-delete-page.html', context)
