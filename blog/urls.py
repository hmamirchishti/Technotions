from django.conf.urls import url,include
from django.views.generic import ListView, DetailView
from . import views
from blog.models import Post

urlpatterns = [
    url(r'^$', ListView.as_view(
        model = Post,
        queryset=Post.objects.all().order_by("-created"),
        paginate_by = '5',
        template_name="blogtemplates/blog.html",
        context_object_name = "posts"
        )),
    url(r'^(?P<pk>\d+)$',DetailView.as_view(model = Post, template_name="blogtemplates/post.html"))
]