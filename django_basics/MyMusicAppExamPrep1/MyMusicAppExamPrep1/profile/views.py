from django.shortcuts import render


# Create your views here.
def profile_details(request):
    return render(request, 'profile/profile-details.html')


def profile_delete(request):
    return render(request, 'profile/profile-delete.html')
