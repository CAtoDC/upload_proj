# Generated by Django 3.1.6 on 2021-02-06 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csvs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='csv',
            old_name='file_name',
            new_name='filename',
        ),
    ]