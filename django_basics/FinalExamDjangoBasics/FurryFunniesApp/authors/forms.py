from django import forms

from FurryFunniesApp.authors.models import Author


class BaseAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'passcode': forms.TextInput(attrs={'placeholder': 'Enter 6 digits...'}),
            'pets_number': forms.NumberInput(attrs={'placeholder': 'Enter the number of your pets...'}),
            'info': forms.Textarea(),
            'image_url': forms.URLInput()
        }

        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'passcode': 'Passcode:',
            'pets_number': 'Pets Number:',
            'info': 'Info:',
            'image_url': 'Profile Image URL:',

        }

        help_texts = {
            'passcode': 'Your passcode must be a combination of 6 digits',
        }


class AuthorCreateForm(BaseAuthorForm):
    class Meta(BaseAuthorForm.Meta):
        exclude = ('info', 'image_url')


class AuthorUpdateForm(BaseAuthorForm):
    class Meta(BaseAuthorForm.Meta):
        exclude = ('passcode',)
