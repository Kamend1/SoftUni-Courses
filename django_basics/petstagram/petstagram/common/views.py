from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import ListView
from pyperclip import copy

from petstagram.photos.models import Photo
from petstagram.common.models import Like
from petstagram.common.forms import CommentForm, SearchForm


# Create your views here.
class HomePageView(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'all_photos'
    paginate_by = 1

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['comment_form'] = CommentForm()
        context['search_form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pet_name = self.request.GET.get('pet_name')

        if pet_name:
            queryset = queryset.filter(
                tagged_pets__name__icontains=pet_name
            )

        return queryset

# def home_page(request):
#     all_photos = Photo.objects.all()
#     comment_form = CommentForm()
#     search_form = SearchForm()
#
#     if request.method == 'POST':
#         if search_form.is_valid():
#             all_photos = all_photos.filter(
#                 tagged_pets__name__icontains=search_form.cleaned_data['pet_name']
#             )
#
#     photos_per_page = 10
#     paginator = Paginator(all_photos, photos_per_page)
#     page = request.GET.get('page')
#
#     try:
#         all_photos = paginator.page(page)
#     except PageNotAnInteger:
#         all_photos = paginator.page(1)
#     except EmptyPage:
#         all_photos = paginator.page(paginator.num_pages)
#
#     context = {
#         'all_photos': all_photos,
#         'comment_form': comment_form,
#         'search_form': search_form,
#     }
#
#     return render(request, 'common/home-page.html', context=context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo-details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(id=photo_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")
