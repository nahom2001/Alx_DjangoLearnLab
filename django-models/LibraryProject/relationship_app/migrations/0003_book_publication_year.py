# Generated by Django 5.1.6 on 2025-07-19 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0002_alter_book_author_alter_librarian_library_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
