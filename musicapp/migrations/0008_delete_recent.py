# Generated by Django 3.0.8 on 2021-01-19 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0007_delete_favourite'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Recent',
        ),
    ]
