# Generated by Django 5.0.1 on 2024-02-02 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0013_alter_book_publication_datetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publication_datetime',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='book',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
