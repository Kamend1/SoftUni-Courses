from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from FurryFunniesApp.authors.models import Author
from FurryFunniesApp.authors.forms import AuthorCreateForm, AuthorUpdateForm
from FurryFunniesApp.utils import get_author_object


# Create your views here.
class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'authors/create-author.html'
    success_url = reverse_lazy('dashboard')


class AuthorUpdate(UpdateView):
    model = Author
    form_class = AuthorUpdateForm
    template_name = 'authors/edit-author.html'
    success_url = reverse_lazy('details-author')

    def get_object(self, queryset=None):
        return get_author_object()


class AuthorDetails(DetailView):
    model = Author
    template_name = 'authors/details-author.html'
    context_object_name = 'author'

    def get_object(self, queryset=None):
        return get_author_object()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.get_object().post_set.exists():
            context['last_updated_post'] = self.get_object().post_set.order_by('updated_at').last().title
        return context


class AuthorDelete(DeleteView):
    model = Author
    template_name = 'authors/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_author_object()
