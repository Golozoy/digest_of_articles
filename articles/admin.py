from django.contrib import admin

from .models import ArticleModel, AuthorModel, FileModel


admin.site.register(ArticleModel)
admin.site.register(AuthorModel)
admin.site.register(FileModel)
