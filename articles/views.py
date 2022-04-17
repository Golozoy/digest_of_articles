from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.contrib.auth.models import AnonymousUser

from .models import ArticleModel
from .serializers import ArticleListSerializer, ArticleRetrieveSerializer


class ArticleListView(ListAPIView):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleListSerializer


class ArticleRetieveView(RetrieveAPIView):
    serializer_class = ArticleRetrieveSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ArticleModel.objects.all()
        else:
            return ArticleModel.objects.filter(is_published=True)
