from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from MyPlantAppExamPrep3.plants.models import Plant
from MyPlantAppExamPrep3.plants.forms import PlantCreateForm, PlantDeleteForm, PlantUpdateForm


# Create your views here.
def home_page(request):
    return render(request, 'plants/home-page.html')


class CatalogueView(ListView):
    model = Plant
    context_object_name = 'plants_list'
    template_name = 'plants/catalogue.html'


class PlantCreate(CreateView):
    model = Plant
    template_name = 'plants/create-plant.html'
    form_class = PlantCreateForm
    success_url = reverse_lazy('catalogue')


class PlantUpdate(UpdateView):
    model = Plant
    template_name = 'plants/edit-plant.html'
    form_class = PlantUpdateForm
    success_url = reverse_lazy('catalogue')
    pk_url_kwarg = 'pk'


class PlantDelete(DeleteView):
    model = Plant
    template_name = 'plants/delete-plant.html'
    success_url = reverse_lazy('catalogue')

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PlantDeleteForm(instance=self.get_object(), initial=self.get_object().__dict__)
        return context


class PlantDetails(DetailView):
    model = Plant
    context_object_name = 'plant'
    template_name = 'plants/plant-details.html'
    pk_url_kwarg = 'pk'
