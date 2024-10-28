from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(5),],
        unique=True,
        error_messages={
            'unique': 'Oops! That title is already taken. How about something fresh and fun?',
        },
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        help_text="Share your funniest furry photo URL!",
    )

    content = models.TextField(blank=False, null=False)

    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        to='authors.Author',
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
