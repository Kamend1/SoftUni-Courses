from django import forms
from TastyRecipesAppExamPrep17042024.recipes.models import Recipe
from TastyRecipesAppExamPrep17042024.mixins import ReadOnlyDisablesFieldMixin


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('author',)

    widgets = {
        'title': forms.TextInput(),
        'cuisine_type': forms.Select(),
        'description': forms.Textarea(attrs={'placeholder': 'ingredient1, ingredient2, ...'}),
        'instructions': forms.Textarea(attrs={'placeholder': 'Enter detailed instructions here...'}),
        'cooking_time': forms.NumberInput(),
        'image_url': forms.URLInput(attrs={'placeholder': 'Optional image URL here...'})
    }

    labels = {
        'title': 'Title:',
        'cuisine_type': 'Cuisine Type:',
        'ingredients': 'Ingredients:',
        'instructions': 'Instructions:',
        'cooking_time': 'Cooking Time:',
        'image_url': 'Image URL:',
    }

    help_texts = {
        'ingredients': 'Ingredients must be separated by a comma and space.',
        'cooking_time': 'Provide the cooking time in minutes.'
    }


class RecipeCreateForm(RecipeBaseForm):
    pass


class RecipeUpdateForm(RecipeBaseForm):
    pass


class RecipeDeleteForm(RecipeBaseForm, ReadOnlyDisablesFieldMixin):
    read_only_and_disabled_fields = ['title',
                                     'cuisine_type',
                                     'description', 'ingredients', 'instructions', 'cooking_time', 'image_url']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ReadOnlyDisablesFieldMixin.__init__(self, *args, **kwargs)