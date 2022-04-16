from django.contrib import admin

from .models import ArticleModel, AuthorModel, FileModel


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'time_updated', 'is_published')
    list_display_links = ('id', 'title', 'slug')
    list_editable = ('is_published',)
    list_filter = ('id', 'title', 'slug', 'is_published', 'time_created')
    list_per_page = 30
    ordering = ('title',)
    search_fields = ('title', 'slug', 'time_updated')
    prepopulated_fields = {"slug": ("title",)}


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'slug')
    list_display_links = ('id', 'nickname', 'slug')
    list_filter = ('id', 'nickname', 'slug')
    list_per_page = 30
    ordering = ('nickname',)
    search_fields = ('nickname', 'slug')
    prepopulated_fields = {"slug": ("nickname",)}


admin.site.register(ArticleModel, ArticleAdmin)
admin.site.register(AuthorModel, AuthorAdmin)
admin.site.register(FileModel)
