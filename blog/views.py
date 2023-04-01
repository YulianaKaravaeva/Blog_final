from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView # new
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView  # new
from django.urls import reverse_lazy, reverse  # new

from .forms import CommentForm
from .models import Post, Comment


class PostListView(ListView):
    paginate_by = 3
    model = Post
    template_name = "home.html"

# форма передавалась в шаблон с контекстом.
# Мы также переименовываем ее в PostDisplay, чтобы указать, что мы обрабатываем только запросы GET.
class PostDisplay(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

# Документация Django предлагает подклассу FormView получить функциональность обработки форм и объединить ее с
# SingleObjectMixin, чтобы получить сообщение, на которое будет ссылаться закрытый ключ как часть URL.
class PostComment(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = 'post_detail.html'

    # переопределить post() метод для загрузки объекта
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(PostComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    # Для правильной обработки данных формы и сохранения нового комментария в базе данных используется form_valid()
    # метод, который вызывается после успешного завершения проверки формы
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)

    # После успешной обработки данных формы пользователь будет перенаправлен на URL, предоставленный get_success_url()
    def get_success_url(self):
        post = self.get_object()
        return reverse('post_detail', kwargs={'pk': post.pk}) + '#comments'


class PostDetailView(View):

    def get(self, request, *args, **kwargs):
        view = PostDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(request, *args, **kwargs)


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


class CommentDeleteView(DeleteView): # new
    model = Comment
    template_name = "comment_delete.html"
    success_url = reverse_lazy("home")

