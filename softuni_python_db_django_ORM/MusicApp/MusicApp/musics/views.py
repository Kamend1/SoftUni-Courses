from django.http import HttpResponse
from django.shortcuts import render, redirect
from MusicApp.common.session_decorator import session_decorator
from MusicApp.settings import session
from MusicApp.musics.models import Album, Song
from MusicApp.musics.forms import AlbumAddForm, AlbumEditForm, AlbumDeleteForm, SongCreateForm


# Create your views here.


@session_decorator(session)
def index(request):
    albums = session.query(Album).all()

    context = {
        'albums': albums
    }

    return render(request, 'common/index.html', context)


@session_decorator(session)
def album_details(request, id):
    album = session.query(Album).filter_by(id=id).first()

    context = {
        'album': album
    }

    return render(request, 'albums/album-details.html', context)


def create_album(request):
    if request.method == 'POST':
        form = AlbumAddForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')

    else:
        form = AlbumAddForm()

    context = {
        'form': form,
    }

    return render(request, 'albums/create-album.html', context)


def delete_album(request, id: int):
    album = (
        session.query(Album)
        .filter_by(id=id)
        .first()
    )

    if request.method == "GET":
        form = AlbumDeleteForm(initial={
            "album_name": album.album_name,
            "image_url": album.image_url,
            "price": album.price,
        })
    else:
        session.delete(album)
        return redirect('index')

    context = {
        "album": album,
        "form": form
    }

    return render(request, 'albums/delete-album.html', context)


@session_decorator(session)
def edit_album(request, id):
    album = session.query(Album).filter_by(id=id).first()

    if request.method == 'POST':
        form = AlbumEditForm(request.POST)
        if form.is_valid():
            album.name = form.cleaned_data['name']
            album.image_url = form.cleaned_data['image_url']
            album.price = form.cleaned_data['price']

        return redirect('index')

    else:
        initial_data = {
            'name': album.name,
            'image_url': album.image_url,
            'price': album.price,
        }

        form = AlbumEditForm(initial_data)

    context = {
        'album': album,
        'form': form,
    }

    return render(request, 'albums/edit-album.html', context)


def create_song(request):
    if request.method == "GET":
        form = SongCreateForm()
    else:
        form = SongCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(request)
            return redirect('index')

    context = {
        "form": form,
    }

    return render(request, 'songs/create-song.html', context)


@session_decorator(session)
def play_song(request, pk):
    song = (
        session.query(Song)
        .filter(Song.id == pk)
        .first()
    )

    context = {
        "song": song,
    }

    return render(request, 'songs/music-player.html', context)


@session_decorator(session)
def serve_song(request, pk):
    song = (
        session.query(Song)
        .filter(Song.id == pk)
        .first()
    )

    if song:
        response = HttpResponse(song.music_file_data, content_type="audio/mpeg")
        response["Content-Disposition"] = f'inline; filename="{song.name}"'
        return response
    else:
        return HttpResponse('Song not found', status=404)


from django.shortcuts import render

# Create your views here.
