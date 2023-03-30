from django.urls import path, include
from .views import (
    PostListView,
    PostDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView
)

urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name="post_new"), # new
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"), # new
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"), # new
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"), # new
    path("", PostListView.as_view(), name="home"),
]
