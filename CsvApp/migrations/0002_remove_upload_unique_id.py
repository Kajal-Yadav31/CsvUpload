# Generated by Django 5.0.6 on 2024-08-05 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CsvApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='unique_id',
        ),
    ]
