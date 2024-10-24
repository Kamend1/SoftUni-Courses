from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from FruitipediaExamPrep2.profiles.models import Profile
from FruitipediaExamPrep2.profiles.forms import ProfileCreateForm, ProfileUpdateForm, ProfileDeleteForm
from FruitipediaExamPrep2.utils import get_profile_object


# Create your views here.
class ProfileCreate(CreateView):
    model = Profile
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('dashboard')
    form_class = ProfileCreateForm


class ProfileEdit(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        return get_profile_object()


class ProfileDetails(DetailView):
    model = Profile
    template_name = 'profiles/details-profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_profile_object()


class ProfileDelete(DeleteView):
    model = Profile
    template_name = 'profiles/delete-profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        return get_profile_object()
