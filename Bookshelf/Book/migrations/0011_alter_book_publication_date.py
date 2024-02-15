# Generated by Django 5.0.1 on 2024-02-02 12:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0010_book_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
