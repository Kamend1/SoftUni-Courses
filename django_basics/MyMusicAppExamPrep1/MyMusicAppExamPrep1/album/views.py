from django.shortcuts import render, redirect
from MyMusicAppExamPrep1.album.forms import AlbumAddForm, AlbumEditForm, AlbumDeleteForm
from MyMusicAppExamPrep1.album.models import Album
from MyMusicAppExamPrep1.profile.models import Profile


# Create your views here.
def album_details(request, id):
    album = Album.objects.get(id=id)

    context = {
        'album': album,
    }

    return render(request, 'album/album-details.html', context)


def album_add(request):
    form = AlbumAddForm(request.POST or None)

    if form.is_valid():
        album = form.save(commit=False)
        album.owner = Profile.objects.get(pk=1)
        album.save()

        return redirect('album-details', album.id)

    context = {
        'form': form,
    }

    return render(request, 'album/album-add.html', context)


def album_edit(request, id):
    album = Album.objects.get(id=id)
    form = AlbumEditForm(instance=album, initial=album.__dict__)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'album/album-edit.html')


def album_delete(request, id):
    album = Album.objects.get(id=id)
    form = AlbumDeleteForm(instance=album, initial=album.__dict__)

    if request.method == 'POST':
        album.delete()

    context = {
        'album': album,
        'form': form
    }

    return render(request, 'album/album-delete.html')
