from django import forms
from WorldOfSpeedAppExamPrep24022024.profiles.models import Profile
from WorldOfSpeedAppExamPrep24022024.mixins import ReadOnlyDisabledFieldMixin


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'age': forms.NumberInput(),
            'password': forms.PasswordInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'profile_picture': forms.URLInput(),
        }

        labels = {
            'username': 'Username:',
            'email': 'Email:',
            'age': 'Age:',
            'password': 'Password:',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'profile_picture': 'Profile Picture:',
        }

        help_texts = {
            'age': 'Age requirement: 21 years and above.',
        }


class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ('first_name', 'last_name', 'profile_picture')


class ProfileUpdateForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm, ReadOnlyDisabledFieldMixin):
    read_only_and_disabled_fields = ['username', 'email', 'age', 'age', 'password',
                                     'first_name', 'last_name', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ReadOnlyDisabledFieldMixin.__init__(self, *args, **kwargs)
