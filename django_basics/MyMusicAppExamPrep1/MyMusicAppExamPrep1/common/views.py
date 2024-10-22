from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView
from MyMusicAppExamPrep1.profile.forms import HomeProfileRegistrationForm
from MyMusicAppExamPrep1.album.models import Album
from MyMusicAppExamPrep1.utils import get_object


# Create your views here.
class HomePageView(ListView, BaseFormView):
    model = Album
    form_class = HomeProfileRegistrationForm
    success_url = reverse_lazy('home-page')
    context_object_name = 'album_list'

    def get_template_names(self):
        profile = get_object()

        if profile:
            return ['common/home-with-profile.html']
        else:
            return ['common/home-no-profile.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
