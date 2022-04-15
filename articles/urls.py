from django.urls import path, include

from .views import ArticleListView, ArticleRetieveView

urlpatterns = [
    path('articles/', ArticleListView.as_view()),
    path('articles/<slug:slug>/', ArticleRetieveView.as_view()),
]

