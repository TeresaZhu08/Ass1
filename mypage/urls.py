from django.urls import path, include
from rest_framework import routers
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from .api import PostViewSet

router = routers.DefaultRouter()
router.register('api/posts', PostViewSet, 'posts')

urlpatterns = [
    path('', PostListView.as_view(), name='MyPage'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('', include(router.urls)),
]





