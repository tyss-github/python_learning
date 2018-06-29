# coding:utf-8

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer
from .serializers import ArticleSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Article


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        article = self.get_object()
        return Response(article.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
