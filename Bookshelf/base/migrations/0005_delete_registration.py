# Generated by Django 5.0.1 on 2024-02-04 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_registration_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Registration',
        ),
    ]