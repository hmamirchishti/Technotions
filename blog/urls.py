from django.conf.urls import url,include
from django.views.generic import ListView, DetailView
from . import views
from blog.models import Post

urlpatterns = [
#        url(r'^posts$', ListView.as_view(
#        model = Post,
#        queryset=Post.objects.all().order_by("-created"),
#        paginate_by = '3',
#        template_name="blogtemplates/blog.html",
#        context_object_name = "posts"
#        )),
    url(r'^$', views.posts),
    url(r'^posts/(?P<pk>\d+)$',DetailView.as_view(model = Post, template_name="blogtemplates/post.html")),
    url(r'^get_categories$', views.get_categories)
   #TODO add url for category
]