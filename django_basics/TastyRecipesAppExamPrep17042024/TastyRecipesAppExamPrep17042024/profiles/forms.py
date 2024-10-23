from django import forms
from TastyRecipesAppExamPrep17042024.profiles.models import Profile
from TastyRecipesAppExamPrep17042024.mixins import ReadOnlyDisablesFieldMixin


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('bio',)

        widgets = {
            'nickname': forms.TextInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'chef': forms.CheckboxInput(attrs={'checked': False}),
        }

        labels = {
            'nickname': 'Nickname:',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'chef': 'Chef:',
        }


class ProfileCreateForm(BaseProfileForm):
    pass


class ProfileEditForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        model = Profile
        exclude = ()

        widgets = {
            **BaseProfileForm.Meta.widgets,
            'bio': forms.Textarea(),  # Add a widget for bio if needed
        }

        labels = {
            **BaseProfileForm.Meta.labels,
            'bio': 'Bio:',
        }


class ProfileDeleteForm(BaseProfileForm, ReadOnlyDisablesFieldMixin):
    read_only_and_disabled_fields = ['nickname', 'first_name', 'last_name', 'chef',]
