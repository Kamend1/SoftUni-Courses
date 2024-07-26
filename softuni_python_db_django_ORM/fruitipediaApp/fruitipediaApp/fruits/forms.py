from django import forms
from fruitipediaApp.fruits.models import Fruit, Category


class BaseCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Category Name'})}


class CategoryAddForm(BaseCategoryForm):
    pass


class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
                   'Image_url': forms.URLInput(attrs={'placeholder': 'Enter Image URL'}),
                   'description': forms.TextInput(attrs={'placeholder': 'Enter fruit description'}),
                   'nutrition': forms.TextInput(attrs={'placeholder': 'Enter description of food nutrition qualities'}),
                   }


class FruitAddForm(BaseFruitForm):
    pass


class FruitEditForm(BaseFruitForm):
    pass


class FruitDeleteForm(BaseFruitForm):
    pass
