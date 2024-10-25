from django import forms

from MyPlantAppExamPrep3.plants.models import Plant
from MyPlantAppExamPrep3.mixins import ReadOnlyDisabledFieldsMixin


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'

        widgets = {
            'type': forms.Select(),
            'name': forms.TextInput(),
            'image_url': forms.URLInput(),
            'description': forms.Textarea(),
            'price': forms.NumberInput(attrs={'step': 0.01}),
        }

        labels = {
            'type': "Type:",
            'name': "Name:",
            'image_url': "Image URL:",
            'description': "Description:",
            'price': "Price:",
        }


class PlantCreateForm(PlantBaseForm):
    pass


class PlantUpdateForm(PlantBaseForm):
    pass


class PlantDeleteForm(PlantBaseForm, ReadOnlyDisabledFieldsMixin):
    ReadOnlyDisabledFields = ['type', 'name', 'image_url', 'description', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_read_only_disabled()
