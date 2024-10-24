from django import forms

from FruitipediaExamPrep2.fruits.models import Fruit
from FruitipediaExamPrep2.mixins import ReadOnlyDisabledFormFieldsMixin


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ('owner',)

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name:'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL:'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description:'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Infor:'}),
        }


class FruitCreateForm(FruitBaseForm):
    pass


class FruitEditForm(FruitBaseForm):
    class Meta(FruitBaseForm.Meta):

        labels = {
            'name': 'Name:',
            'image_url': 'Image URL:',
            'description': 'Description:',
            'nutrition': 'Nutrition:',
        }


class FruitDeleteForm(FruitBaseForm, ReadOnlyDisabledFormFieldsMixin):
    ReadOnlyDisabledFormFields = ['name', 'image_url', 'description']

    class Meta(FruitBaseForm.Meta):
        exclude = ('owner', 'nutrition',)

        labels = {
            'name': 'Name:',
            'image_url': 'Image URL:',
            'description': 'Description:',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_readonly_disabled()
