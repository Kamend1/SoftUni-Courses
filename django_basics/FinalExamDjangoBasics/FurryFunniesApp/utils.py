from FurryFunniesApp.authors.models import Author


def get_author_object():
    return Author.objects.all().first()
