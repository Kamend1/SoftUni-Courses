from django import forms

from MyMusicAppExamPrep1.album.models import Album


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner',)

        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'genre': forms.MultipleChoiceField(),
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


class AlbumDeleteForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
