# Generated by Django 4.2 on 2023-04-19 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Author Name')),
                ('email', models.EmailField(max_length=255, verbose_name='Author Email Address')),
                ('bio', models.TextField(verbose_name='Author Biography')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category Name')),
                ('description', models.TextField(verbose_name='Category Description')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Article Title')),
                ('content', models.TextField(verbose_name='Article content')),
                ('published_on', models.DateField(verbose_name='Publish Date')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.author')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.category')),
            ],
        ),
    ]