from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView
from MyMusicAppExamPrep1.utils import get_object
from MyMusicAppExamPrep1.profile.forms import ProfileDeleteForm


# Create your views here.
class ProfileDetailsView(DetailView):
    template_name = 'profile/profile-details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_object()


class ProfileDeleteView(DeleteView):
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return get_object()
