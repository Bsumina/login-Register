# Generated by Django 5.0.1 on 2024-02-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0012_remove_book_publication_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
