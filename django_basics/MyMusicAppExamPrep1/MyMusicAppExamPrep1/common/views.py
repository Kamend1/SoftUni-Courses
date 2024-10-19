from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from MyMusicAppExamPrep1.common.forms import HomeProfileRegistrationForm
from MyMusicAppExamPrep1.profile.models import Profile


# Create your views here.
class HomePageView(FormView):
    template_name = 'common/home-no-profile.html'
    form_class = HomeProfileRegistrationForm
    success_url = reverse_lazy('home-page')  # Redirect to the same page after POST

    def form_valid(self, form):
        username = form.cleaned_data['username']
        profile = Profile.objects.filter(username=username).first()

        if not profile:
            # Save the profile if it doesn't exist
            profile = form.save()

        # Fetch all albums related to this profile
        all_albums = profile.album_set.all()

        # Render the template with profile and albums if user exists
        return render(self.request, 'common/home-with-profile.html', {
            'profile': profile,
            'form': form,
            'all_albums': all_albums,
        })

    def form_invalid(self, form):
        # Handle the case where the form is invalid
        return self.render_to_response(self.get_context_data(form=form))


def home_page(request):
    form = HomeProfileRegistrationForm(request.POST or None)
    profile = None

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            profile = Profile.objects.filter(username=username).first()

            if not profile:
                profile = form.save()

            all_albums = profile.album_set.all()

            context = {
                'profile': profile,
                'form': form,
                'all_albums': all_albums,
            }
            return render(request, 'common/home-with-profile.html', context)

    context = {
        'form': form,
    }
    return render(request, 'common/home-no-profile.html', context)