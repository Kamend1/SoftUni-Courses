from django.shortcuts import render, get_object_or_404


# Create your views here.
def register(request):
    return render(request, 'accounts/register-page.html')


def login(request):
    return render(request, 'accounts/login-page.html')


def show_profile_details(request, pk):

    # profile = User.objects.filter(pk=pk).first()

    context = {
        'pk': pk,
    }

    return render(request, 'accounts/profile-details-page.html', context)


def edit_profile(request, pk):
    context = {
        'pk': pk
    }

    return render(request, 'accounts/profile-edit-page.html', context)


def delete_profile(request, pk):
    context = {
        'pk': pk
    }

    return render(request, 'accounts/profile-delete-page.html', context)
