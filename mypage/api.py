from .models import Post
from rest_framework import viewsets, permissions
from .serializers import PostSerializer
from rest_framework import mixins


class PostListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer


class PostCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer


class PostRetrieveViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()


class PostUpdateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()


class PostDeleteViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()




