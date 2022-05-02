from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import ArticleModel
from .serializers import ArticleListSerializer, ArticleRetrieveSerializer


class ArticleListView(ListAPIView):
    """Список всех статей."""
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleListSerializer


class ArticleRetieveView(RetrieveAPIView):
    """Конкретная статья"""
    serializer_class = ArticleRetrieveSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ArticleModel.objects.all()
        else:
            return ArticleModel.objects.filter(is_published=True)


class ArticleFilterListView(ListAPIView):
    """Список статей с частичным совпадением url"""
    serializer_class = ArticleListSerializer

    def get_queryset(self):
        return ArticleModel.objects.filter(slug__icontains=self.kwargs['slug'])
