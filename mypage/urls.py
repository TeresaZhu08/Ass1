from django.urls import path, include
from rest_framework import routers
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from .api import PostListViewSet, PostCreateViewSet, PostRetrieveViewSet, PostUpdateViewSet, PostDeleteViewSet

router = routers.DefaultRouter()
router.register('posts', PostListViewSet, 'posts')
router.register('posts/new', PostCreateViewSet, 'create')
router.register('posts/<int:pk>', PostRetrieveViewSet, 'detail')
router.register('posts/<int:pk>/update', PostUpdateViewSet, 'update')
router.register('posts/<int:pk>/delete', PostDeleteViewSet, 'delete')

urlpatterns = [
    path('', PostListView.as_view(), name='MyPage'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/create', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('api/', include(router.urls)),

]
