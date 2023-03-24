from django.shortcuts import render
from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # new
from django.urls import reverse_lazy # new

from .models import Post
from .forms import CommentForm


def post_detail(request, post):
    # List of active comments for this post
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'post_detail.html',
                 {'post': post,
                  'comments': comments,
                  'comment_form': comment_form})


class BlogListView(ListView):
    paginate_by = 3
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView): # new
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView): # new
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView): # new
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]


class BlogDeleteView(DeleteView): # new
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")

