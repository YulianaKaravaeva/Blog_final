from django.urls import path, include
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView, # new
)
# from django.contrib.auth.models import User
# from django.core.paginator import Paginator
#
# users = User.objects.all()
#
# paginator = Paginator(users, 10)
#
# page_obj = paginator.get_page(99)
#
# print(page_obj)

urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name="post_new"), # new
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"), # new
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"), # new
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"), # new
    path("", BlogListView.as_view(), name="home"),
]
