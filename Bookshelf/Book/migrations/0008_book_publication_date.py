# Generated by Django 5.0.1 on 2024-02-02 12:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0007_remove_book_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publication_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
