# Generated by Django 5.0.4 on 2024-07-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_review_article_alter_review_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(related_name='articles', to='main_app.author'),
        ),
    ]
