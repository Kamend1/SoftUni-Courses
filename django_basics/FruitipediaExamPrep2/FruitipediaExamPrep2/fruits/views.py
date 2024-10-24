from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from FruitipediaExamPrep2.fruits.models import Fruit
from FruitipediaExamPrep2.fruits.forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from FruitipediaExamPrep2.utils import get_profile_object


# Create your views here.
class DashboardView(ListView):
    model = Fruit
    context_object_name = 'fruit_list'
    template_name = 'fruits/dashboard.html'


class FruitCreate(CreateView):
    model = Fruit
    template_name = 'fruits/create-fruit.html'
    form_class = FruitCreateForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner = get_profile_object()
        return super().form_valid(form)


class FruitEdit(UpdateView):
    model = Fruit
    template_name = 'fruits/edit-fruit.html'
    form_class = FruitEditForm
    success_url = reverse_lazy('dashboard')
    pk_url_kwarg = 'pk'


class FruitDelete(DeleteView):
    model = Fruit
    template_name = 'fruits/delete-fruit.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        fruit = self.model.objects.get(pk=self.kwargs['pk'])
        return fruit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FruitDeleteForm(instance=self.get_object(), initial=self.get_object().__dict__)
        return context


class FruitDetails(DetailView):
    model = Fruit
    context_object_name = 'fruit'
    pk_url_kwarg = 'pk'
    template_name = 'fruits/details-fruit.html'
