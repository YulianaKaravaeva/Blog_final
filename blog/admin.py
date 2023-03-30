from django.contrib import admin
from .models import Post, Comment

# С помощью CommentInline подклассов admin.StackedInline,
# которые могут отображаться и редактироваться вместе с публикацией, к которой они принадлежат.


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Post, PostAdmin)

#admin.site.register(Post)
#admin.site.register(Comment)
