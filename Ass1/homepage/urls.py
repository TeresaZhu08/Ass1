from django.conf.urls import url
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


def trigger_error(request):
    division_by_zero = 1 / 0


def my_function(request):
    return "ok"


urlpatterns = {
    path('sentry-debug/', trigger_error),
    path('', PostListView.as_view(), name='homepage'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    url(r"^myurl/(?P<myid>\d+)/$", my_function)
}

handler404 = 'homepage.views.homepage_not_found_view'