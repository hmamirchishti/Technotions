from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Categories, Post
def index(request):
    categories = GetCategories()
    return render(request,'blogtemplates/header.html',
                  {'categories': categories})
  
def posts (request):
  paginator = Paginator(GetPosts(), 2)
  page = request.GET.get('page')
  try:
     posts = paginator.page(page)
  except PageNotAnInteger:
      posts = paginator.page(1)
  except EmptyPage:
        posts = paginator.page(paginator.num_pages)
  
  return render(request, 'blogtemplates/blog.html', {'categories': GetCategories(),'posts': posts})

def get_categories(request):
 #   categories = json.dumps(Categories.objects.all())    
  #  return HttpResponse(categories)
  data = serializers.serialize('json', Categories.objects.all())
  return HttpResponse(data, content_type="application/json")

def GetCategories():
  return Categories.objects.all()

def GetPosts():
  return Post.objects.all().order_by("-created")

			