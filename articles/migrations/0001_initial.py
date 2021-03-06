# Generated by Django 4.0.4 on 2022-04-19 04:16

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(db_index=True, max_length=255, verbose_name='Авторы')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ['nickname'],
            },
        ),
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(db_index=True, upload_to=articles.models.path_to_upload_file, verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Заголовок')),
                ('annotation', models.CharField(max_length=255, verbose_name='Аннотация')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('body', models.TextField(verbose_name='Статья')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_updated', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('authors', models.ManyToManyField(to='articles.authormodel', verbose_name='Автор')),
                ('files', models.ManyToManyField(to='articles.filemodel', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ['title', 'time_created'],
            },
        ),
    ]
