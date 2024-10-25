from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from MyPlantAppExamPrep3.plants.models import Plant
from MyPlantAppExamPrep3.profiles.forms import ProfileCreateForm, ProfileUpdateForm
from MyPlantAppExamPrep3.profiles.models import Profile
from MyPlantAppExamPrep3.utils import get_profile_object


# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    success_url = reverse_lazy('catalogue')
    template_name = 'profiles/create-profile.html'


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('details-profile')

    def get_object(self, queryset=None):
        return get_profile_object()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profiles/delete-profile.html'
    success_url = reverse_lazy('home_page')

    def get_object(self, queryset=None):
        return get_profile_object()


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile_object()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plants = Plant.objects.all()
        context['plants'] = plants
        return context