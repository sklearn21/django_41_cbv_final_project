# Generated by Django 3.1.7 on 2021-03-19 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beer',
            old_name='test',
            new_name='taste',
        ),
    ]
