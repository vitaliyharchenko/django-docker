from .models import Post
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin


admin.site.register(Post, MarkdownxModelAdmin)
