from django.core.validators import MinLengthValidator
from django.db import models


class ContentPublishedOnMixin(models.Model):
    content = models.TextField(
        validators=[
            MinLengthValidator(10)
        ],
    )

    published_on = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True
