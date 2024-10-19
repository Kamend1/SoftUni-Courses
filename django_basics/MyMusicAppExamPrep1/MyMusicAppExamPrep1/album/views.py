from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from MyMusicAppExamPrep1.album.forms import AlbumAddForm, AlbumEditForm, AlbumDeleteForm
from MyMusicAppExamPrep1.album.models import Album
from MyMusicAppExamPrep1.profile.models import Profile


# Create your views here.
class AlbumDetailsView(DetailView):
    model = Album
    template_name = 'album/album-details.html'
    context_object_name = 'album'


class AlbumAddView(CreateView):
    model = Album
    template_name = 'album/album-add.html'
    form_class = AlbumAddForm
    context_object_name = 'album'

    def get_success_url(self):
        return reverse_lazy('album-details', kwargs={'pk': self.object.pk})


class AlbumEditView(UpdateView):
    model = Album
    form_class = AlbumEditForm
    template_name = 'album/album-edit.html'

    def get_success_url(self):
        return reverse_lazy('album-details', kwargs={'pk': self.object.pk})


class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'album/album-delete.html'
    success_url = 'common/home-with-profile.html'

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AlbumDeleteForm(initial=self.object.__dict__)
        return context


# def album_details(request, id):
#     album = Album.objects.get(id=id)
#
#     context = {
#         'album': album,
#     }
#
#     return render(request, 'album/album-details.html', context)


# def album_add(request):
#     form = AlbumAddForm(request.POST or None)
#
#     if form.is_valid():
#         album = form.save(commit=False)
#         album.owner = Profile.objects.get(pk=1)
#         album.save()
#
#         return redirect('album-details', album.id)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'album/album-add.html', context)


# def album_edit(request, id):
#     album = Album.objects.get(id=id)
#     form = AlbumEditForm(instance=album, initial=album.__dict__)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#
#     context = {
#         'form': form,
#         'album': album,
#     }
#
#     return render(request, 'album/album-edit.html', context)


# def album_delete(request, id):
#     album = Album.objects.get(id=id)
#     form = AlbumDeleteForm(instance=album, initial=album.__dict__)
#
#     if request.method == 'POST':
#         album.delete()
#
#     context = {
#         'album': album,
#         'form': form
#     }
#
#     return render(request, 'album/album-delete.html', context)
