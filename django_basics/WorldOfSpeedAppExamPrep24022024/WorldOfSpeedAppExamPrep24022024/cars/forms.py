from django import forms
from WorldOfSpeedAppExamPrep24022024.cars.models import Car
from WorldOfSpeedAppExamPrep24022024.mixins import ReadOnlyDisabledFieldMixin


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner',)

        widgets = {
            'type': forms.Select(),
            'model': forms.TextInput(),
            'year': forms.NumberInput(),
            'image_url': forms.URLInput(attrs={'placeholder': 'http://...'}),
            'price': forms.NumberInput(),
        }

        labels = {
            'type': 'Type:',
            'model': 'Model:',
            'year': 'Year:',
            'image_url': 'Image URL:',
            'price': 'Price:',
        }


class CarCreateForm(CarBaseForm):
    pass


class CarUpdateForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm, ReadOnlyDisabledFieldMixin):
    read_only_and_disabled_fields = ['type', 'model', 'year', 'image_url', 'price',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ReadOnlyDisabledFieldMixin.__init__(self, *args, **kwargs)
