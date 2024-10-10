from django.db import models

from petstagram.photos.models import Photo


# Create your models here.
class Comment(models.Model):
    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['date_time_of_publication']),
        ]
        ordering = ['-date_time_of_publication']

    def __str__(self):
        return self.text


class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
