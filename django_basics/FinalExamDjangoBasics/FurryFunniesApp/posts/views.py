from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView

from FurryFunniesApp.posts.models import Post
from FurryFunniesApp.posts.forms import PostCreateForm, PostUpdateForm, PostDeleteForm
from FurryFunniesApp.utils import get_author_object


# Create your views here.
class CreatePost(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = get_author_object()
        return super().form_valid(form)


class EditPost(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dashboard')
    pk_url_kwarg = 'pk'


class DeletePost(DeleteView):
    model = Post
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostDeleteForm(instance=self.get_object(), initial=self.get_object().__dict__)
        return context


class DetailsPost(DetailView):
    model = Post
    pk_url_kwarg = 'pk'
    template_name = 'posts/details-post.html'
    context_object_name = 'post'
