# Generated by Django 5.0.1 on 2024-02-02 13:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0011_alter_book_publication_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publication_date',
        ),
        migrations.AddField(
            model_name='book',
            name='publication_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
