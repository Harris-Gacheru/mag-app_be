# Generated by Django 4.2 on 2023-04-19 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='category_id',
            new_name='category',
        ),
    ]
