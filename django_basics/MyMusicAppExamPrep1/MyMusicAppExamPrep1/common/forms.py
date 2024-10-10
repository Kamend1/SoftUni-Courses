from django import forms

from MyMusicAppExamPrep1.profile.models import Profile


class HomeProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
        }

        labels = {
            'username': 'Username:',
            'email': 'Email:',
            'age': 'Age:',
        }

