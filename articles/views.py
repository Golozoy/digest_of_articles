from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import ArticleModel
from .serializers import ArticleListSerializer, ArticleRetrieveSerializer


class ArticleListView(ListAPIView):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleListSerializer


class ArticleRetieveView(RetrieveAPIView):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleRetrieveSerializer
    lookup_field = 'slug'
