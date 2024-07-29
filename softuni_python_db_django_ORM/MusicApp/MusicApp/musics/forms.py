from django import forms
from MusicApp.common.session_decorator import session_decorator
from MusicApp.settings import session
from MusicApp.musics.models import Album, Song

class BaseAlbumForm(forms.Form):
    name = forms.CharField(label='Album name', max_length=50, required=True)
    image_url = forms.URLField(label='Enter Image URL', max_length=255, required=True)
    price = forms.DecimalField(label='Price', decimal_places=2, min_value=0.0, required=True)


class AlbumAddForm(BaseAlbumForm):
    @session_decorator(session)
    def save(self):
        new_album = Album(
            name=self.cleaned_data['name'],
            image_url=self.cleaned_data['image_url'],
            price=self.cleaned_data['price'],
        )

        session.add(new_album)


class AlbumDeleteForm(BaseAlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True


class AlbumEditForm(BaseAlbumForm):
    pass


class SongBaseForm(forms.Form):
    name = forms.CharField(
        label="Song Name:",
        max_length=10,
        required=True
    )

    album = forms.ChoiceField(
        label="Album:",
        choices=[],  # we overwrite that in the init
    )

    music_file_data = forms.FileField(
        label="Music File:",
        required=True,
    )

    @session_decorator(session)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        albums = session.query(Album).all()
        self.fields["album"].choices = [(album.id, album.name) for album in albums]


class SongCreateForm(SongBaseForm):

    @session_decorator(session)
    def save(self, request):
        new_song = Song(
            name=self.cleaned_data['name'],
            album_id=self.cleaned_data['album'],
            music_file_data=request.FILES['music_file_data'].read()
        )

        session.add(new_song)