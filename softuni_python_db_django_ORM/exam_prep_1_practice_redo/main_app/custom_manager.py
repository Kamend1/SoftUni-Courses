from django.db import models
from django.db.models import Count


class CustomDirectorManager(models.Manager):
    def get_directors_by_movies_count(self):

        return self.annotate(num_movies=Count('movies')).order_by('-num_movies', 'full_name')