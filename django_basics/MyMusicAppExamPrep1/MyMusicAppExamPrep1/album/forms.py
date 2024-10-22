from django import forms
from MyMusicAppExamPrep1.album.models import Album
from MyMusicAppExamPrep1.mixins import ReadOnlyDisabledMixin


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner',)

        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'genre': forms.Select(),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                    'step': '0.01',
                },
            ),
        }

        labels = {
            'album_name': 'Album Name:',
            'artist': 'Artist:',
            'genre': 'Genre:',
            'description': 'Description:',
            'image': 'Image URL:',
            'price': 'Price:',
        }


class AlbumAddForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(AlbumBaseForm, ReadOnlyDisabledMixin):
    pass
