from django import forms
from FurryFunniesApp.posts.models import Post
from FurryFunniesApp.mixins import ReadOnlyDisabledFormFieldsMixin


class BasePostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'updated_at')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Put an attractive and unique title...',}),
            'image_url': forms.URLInput(),
            'content': forms.Textarea(attrs={'placeholder': 'Share some interesting facts about your adorable pets...',}),
        }

        labels = {
            'title': 'Title:',
            'image_url': 'Post Image URL:',
            'content': 'Content:',
        }

        help_texts = {
            'image_url': 'Share your funniest furry photo URL!',
        }


class PostCreateForm(BasePostForm):
    pass


class PostUpdateForm(BasePostForm):
    pass


class PostDeleteForm(BasePostForm, ReadOnlyDisabledFormFieldsMixin):
    ReadOnlyDisabledFormFields = ['title', 'image_url', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_readonly_disabled()
