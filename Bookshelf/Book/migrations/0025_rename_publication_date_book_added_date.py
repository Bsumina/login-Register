# Generated by Django 5.0.1 on 2024-02-03 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0024_alter_book_publication_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publication_date',
            new_name='added_date',
        ),
    ]
