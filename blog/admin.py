from django.contrib import admin
from blog.models import Post, User, Categories
from markdownx.admin import MarkdownxModelAdmin


class EntryAdmin(MarkdownxModelAdmin):
    list_display = ("title","created","user")
    prepopulated_fields = {"slug":("title",)}
admin.site.register(Post,EntryAdmin)
admin.site.register(User)
admin.site.register(Categories)