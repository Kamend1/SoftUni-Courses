from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from TastyRecipesAppExamPrep17042024.recipes.models import Recipe
from TastyRecipesAppExamPrep17042024.recipes.forms import RecipeCreateForm, RecipeUpdateForm, RecipeDeleteForm
from TastyRecipesAppExamPrep17042024.utils import get_profile_object


# Create your views here.
class CatalogueView(ListView):
    model = Recipe
    template_name = 'recipes/catalogue.html'
    context_object_name = 'recipe_list'


class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'recipes/create-recipe.html'
    success_url = reverse_lazy('catalogue')
    form_class = RecipeCreateForm

    def form_valid(self, form):
        form.instance.author = get_profile_object()
        return super().form_valid(form)


class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = 'recipes/edit-recipe.html'
    form_class = RecipeUpdateForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('catalogue')


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipes/delete-recipe.html'
    form_class = RecipeDeleteForm
    success_url = reverse_lazy('catalogue')

    def get_object(self, queryset=None):
        return Recipe.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipeDeleteForm(initial=self.get_object().__dict__)
        return context


class RecipeDetailsView(DetailView):
    model = Recipe
    pk_url_kwarg = 'pk'
    template_name = 'recipes/details-recipe.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients_list'] = self.object.ingredients.split(',')
        return context
