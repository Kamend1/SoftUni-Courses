from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram.pets.models import Pet
from petstagram.pets.forms import PetAddForm, PetDeleteForm, PetEditForm
from petstagram.common.forms import CommentForm


# Create your views here.
class AddPetView(CreateView):
    model = Pet
    form_class = PetAddForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile-details', kwargs=({'pk':1}))

# def add_pet(request):
#     form = PetAddForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('profile-details', pk=1)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'pets/pet-add-page.html', context)


class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = self.object.photo_set.all()
        context['comment_form'] = CommentForm()
        return context


# def pet_details(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#     all_photos = pet.photo_set.all()
#     comment_form = CommentForm()
#
#     context = {
#         'pet': pet,
#         'all_photos': all_photos,
#         'comment_form': comment_form,
#     }
#
#     return render(request, 'pets/pet-details-page.html', context)


class EditPetView(UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self):
        return reverse_lazy(
            'pet-details',
            kwargs={
                'username': self.kwargs['username'],
                'pet_slug': self.kwargs['pet_slug'],
            }

        )

# def edit_pet(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#
#     if request.method == 'GET':
#         form = PetEditForm(instance=pet, initial=pet.__dict__)
#     else:
#         form = PetEditForm(request.POST, instance=pet)
#         if form.is_valid():
#             form.save()
#             return redirect('pet-details', username, pet_slug)
#
#     context = {
#         'username': username,
#         'pet_slug': pet_slug,
#         'form': form,
#         'pet': pet,
#     }
#
#     return render(request, 'pets/pet-edit-page.html', context)


class DeletePetView(DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    context_object_name = 'pet'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})

    def get_object(self, queryset=None):
        return Pet.objects.get(slug=self.kwargs['pet_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PetDeleteForm(initial=self.object.__dict__)
        return context

    def delete(self, request, *args, **kwargs):
        pet = self.get_object()
        pet.delete()
        return redirect(self.success_url)


# def delete_pet(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#
#     if request.method == 'POST':
#         pet.delete()
#         return redirect('profile-details', pk=1)
#
#     form = PetDeleteForm(initial=pet.__dict__)
#
#     context = {
#         'username': username,
#         'pet_slug': pet_slug,
#         'forms': form,
#         'pet': pet,
#     }
#
#     return render(request, 'pets/pet-delete-page.html', context)
