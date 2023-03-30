from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Comment


class CommentForm(ModelForm):
    # Метакласс определяет модель и поля модели, которые будут использоваться для формы.
    class Meta:
        model = Comment
        fields = ['name', 'comment']

    # сделать запрос доступным для проверки формы
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CommentForm, self).__init__(*args, **kwargs)