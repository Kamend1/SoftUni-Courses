from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from WorldOfSpeedAppExamPrep24022024.profiles.models import Profile
from WorldOfSpeedAppExamPrep24022024.profiles.forms import ProfileCreateForm, ProfileUpdateForm
from WorldOfSpeedAppExamPrep24022024.utils import get_profile_object


# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'profiles/profile-create.html'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('catalogue')


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'

    @staticmethod
    def get_name_if_any():
        name = ""
        if get_profile_object().first_name:
            name += get_profile_object().first_name + " "
        if get_profile_object().last_name:
            name += get_profile_object().last_name

        return name if name else None

    @staticmethod
    def get_total_price():
        return get_profile_object().car_set.aggregate(total=Sum('price'))['total']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile_object()
        context['full_name'] = self.get_name_if_any()
        context['total_price'] = self.get_total_price()
        return context

    def get_object(self, queryset=None):
        return get_profile_object()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile_object()


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'profiles/profile-edit.html'
    success_url = reverse_lazy('profile-details')
    form_class = ProfileUpdateForm

    def get_object(self, queryset=None):
        return get_profile_object()
