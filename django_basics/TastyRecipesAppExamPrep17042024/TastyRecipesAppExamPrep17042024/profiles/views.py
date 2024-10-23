from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from TastyRecipesAppExamPrep17042024.profiles.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from TastyRecipesAppExamPrep17042024.profiles.models import Profile
from TastyRecipesAppExamPrep17042024.utils import get_profile_object


# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('catalogue')


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('catalogue')

    def get_object(self, queryset=None):
        return get_profile_object()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profiles/delete-profile.html'
    success_url = reverse_lazy('home_page')

    def get_object(self, queryset=None):
        return get_profile_object()


class ProfileDetailsView(DetailView):
    template_name = 'profiles/details-profile.html'

    def get_object(self, queryset=None):
        return get_profile_object()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile_object()
        return context
