from django.db.models import Count
from django.db import models


class CustomAuthorManager(models.Manager):

    def get_authors_by_article_count(self):
        return self.annotate(num_articles=Count('articles')).order_by('-num_articles', 'email')