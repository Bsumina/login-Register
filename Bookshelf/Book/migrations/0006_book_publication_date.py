# Generated by Django 5.0.1 on 2024-02-02 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0005_alter_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publication_date',
            field=models.DateField(default='2024-02-02'),
            preserve_default=False,
        ),
    ]
