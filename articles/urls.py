from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import ArticleListView, ArticleRetieveView

urlpatterns = [
    path('articles/', ArticleListView.as_view()),
    path('articles/<slug:slug>/', ArticleRetieveView.as_view()),
    path('auth/', include('djoser.urls')),
    path('jwt/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
