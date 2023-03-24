from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)  # заголовок
    author = models.ForeignKey(  # автор (отношение многие-к-одному)
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    body = models.TextField()

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
