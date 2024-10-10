from django.shortcuts import render, redirect
from MyMusicAppExamPrep1.common.forms import HomeProfileRegistrationForm
from MyMusicAppExamPrep1.profile.models import Profile


# Create your views here.
def home_page(request):
    profile = None
    form = HomeProfileRegistrationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            profile = Profile.objects.get(username=username)

            if not profile:
                form.save()

            all_albums = profile.album_set.all()
            profile = Profile.objects.get(username=username)

            context = {
                'profile': profile,
                'form': form,
                'all_albums': all_albums,
            }
            return render(request,'common/home-with-profile.html', context)

    context = {
        'form': form,
    }
    return render(request, 'common/home-no-profile.html', context)

