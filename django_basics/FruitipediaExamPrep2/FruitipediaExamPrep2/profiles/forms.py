from django import forms

from FruitipediaExamPrep2.profiles.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age', 'default': 18}),
        }

        help_texts = {
            'password': '*Password length requirements: 8 to 20 characters'
        }


class ProfileCreateForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        exclude = ('image_url', 'age',)


class ProfileUpdateForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        exclude = ('email', 'password',)

    labels = {
        'first_name': 'First Name:',
        'last_name': 'Last Name:',
        'image_url': 'Image Url:',
        'age': 'Age:',
    }


class ProfileDeleteForm(BaseProfileForm):
    pass
