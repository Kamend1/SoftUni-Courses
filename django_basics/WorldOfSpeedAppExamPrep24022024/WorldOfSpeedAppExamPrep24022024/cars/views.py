from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from WorldOfSpeedAppExamPrep24022024.cars.forms import CarCreateForm, CarUpdateForm, CarDeleteForm
from WorldOfSpeedAppExamPrep24022024.cars.models import Car
from WorldOfSpeedAppExamPrep24022024.utils import get_profile_object


# Create your views here.
class CatalogueView(ListView):
    template_name = 'cars/catalogue.html'
    model = Car
    context_object_name = 'car_list'


class CarCreateView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'cars/car-create.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.owner = get_profile_object()
        return super().form_valid(form)


class CarDetailsView(DetailView):
    template_name = 'cars/car-details.html'
    model = Car
    pk_url_kwarg = 'pk'
    context_object_name = 'car'


class CarUpdateView(UpdateView):
    model = Car
    pk_url_kwarg = 'pk'
    form_class = CarUpdateForm
    template_name = 'cars/car-edit.html'
    success_url = reverse_lazy('catalogue')


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy('catalogue')

    def get_object(self, queryset=None):
        return self.model.objects.get(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CarDeleteForm(initial=self.get_object().__dict__)
        return context
