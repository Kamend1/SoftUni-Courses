from django.shortcuts import render
from django.views.generic import ListView

from FurryFunniesApp.posts.models import Post


# Create your views here.
def index(request):
    return render(request, 'common/index.html')


class DashboardView(ListView):
    model = Post
    template_name = 'common/dashboard.html'
    context_object_name = 'posts_list'
