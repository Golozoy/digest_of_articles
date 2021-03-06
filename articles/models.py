from django.db import models


def path_to_upload_file(instance, filename):
    return f"{filename}"


class AuthorModel(models.Model):
    nickname = models.CharField(max_length=255, db_index=True, verbose_name='Авторы')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['nickname']


class ArticleModel(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name="Заголовок")
    annotation = models.CharField(max_length=255, verbose_name="Аннотация")
    authors = models.ManyToManyField('AuthorModel', verbose_name="Автор")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    body = models.TextField(verbose_name='Статья')
    files = models.ManyToManyField('FileModel', verbose_name="Файл")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_updated = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['title', 'time_created']


class FileModel(models.Model):
    file = models.FileField(upload_to=path_to_upload_file, db_index=True, verbose_name="Файл")

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
