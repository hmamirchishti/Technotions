from django.contrib import admin
from blog.models import Post, User, Categories
from markdownx.admin import MarkdownxModelAdmin



admin.site.register(Post,MarkdownxModelAdmin)
admin.site.register(User)
admin.site.register(Categories) 