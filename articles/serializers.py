from rest_framework import serializers

from .models import ArticleModel


class ArticleListSerializer(serializers.ModelSerializer):

    authors = serializers.StringRelatedField(many=True)

    class Meta:
        model = ArticleModel
        fields = ['title', 'annotation', 'authors', 'slug', 'time_updated', 'is_published']


class ArticleRetrieveSerializer(serializers.ModelSerializer):

    authors = serializers.StringRelatedField(many=True)
    files = serializers.StringRelatedField(many=True)

    class Meta:
        model = ArticleModel
        fields = ['id', 'title', 'annotation', 'authors', 'slug', 'body', 'files', 'time_created', 'time_updated', 'is_published']
