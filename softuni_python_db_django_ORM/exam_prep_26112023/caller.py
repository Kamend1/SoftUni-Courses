import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()
from django.db.models import Q, F, Count, Avg

# Import your models here
from main_app.models import Author, Article, Review


# Create queries within functions
def get_authors(search_name=None, search_email=None):
    if search_name is None and search_email is None:
        return ""

    name_query = Q(full_name__icontains=search_name)
    email_query = Q(email__icontains=search_email)
    query_set = None

    if search_name is None:
        query_set = Author.objects.filter(email_query).order_by('-full_name')

    if search_email is None:
        query_set = Author.objects.filter(name_query).order_by('-full_name')

    if search_name is not None and search_email is not None:
        query_set = Author.objects.filter(name_query & email_query).order_by('-full_name')

    if not query_set.exists():
        return ""

    result = []

    for a in query_set:
        status = "Banned" if a.is_banned else "Not Banned"
        result.append(f"Author: {a.full_name}, email: {a.email}, status: {status}")

    return '\n'.join(result)


def get_top_publisher():
    top_publisher = Author.objects.get_authors_by_article_count().filter(num_articles__gt=0)[:1]

    if not top_publisher.exists():
        return ""

    return f"Top Author: {top_publisher[0].full_name} with {top_publisher[0].num_articles} published articles."


def get_top_reviewer():
    top_reviewer = Author.objects.annotate(num_reviews=Count('Reviews_Author')).filter(
        num_reviews__gt=0
    ).order_by('-num_reviews', 'email')[:1]

    if not top_reviewer.exists():
        return ""

    return f"Top Reviewer: {top_reviewer[0].full_name} with {top_reviewer[0].num_reviews} published reviews."


def get_latest_article():
    article = Article.objects.prefetch_related(
        'authors', 'Reviews_Article').order_by(
        '-published_on').annotate(
        num_reviews=Count('Reviews_Article'),
        avg_rating=Avg('Reviews_Article__rating')
    ).first()

    if not article:
        return ""

    average_rating = article.avg_rating if article.avg_rating is not None else 0.0

    return (f"The latest article is: {article.title}. "
            f"Authors: {', '.join(a.full_name for a in article.authors.all().order_by('full_name'))}. "
            f"Reviewed: {article.num_reviews} times. "
            f"Average Rating: {average_rating:.2f}.")


def get_top_rated_article():
    article = Article.objects.prefetch_related('Reviews_Article').annotate(
        num_reviews=Count('Reviews_Article'),
        avg_rating=Avg('Reviews_Article__rating'),
    ).filter(num_reviews__gt=0).order_by('-avg_rating', 'title').first()

    if not article:
        return ""

    return (f"The top-rated article is: {article.title}, "
            f"with an average rating of {article.avg_rating:.2f}, "
            f"reviewed {article.num_reviews} times.")


def ban_author(email=None):
    if email is None:
        return "No authors banned."

    author = Author.objects.filter(email=email).first()

    if not author:
        return "No authors banned."

    num_reviews, _ = Review.objects.prefetch_related('authors').filter(author=author).delete()

    author.is_banned = True
    author.save()

    return f"Author: {author.full_name} is banned! {num_reviews} reviews deleted."
