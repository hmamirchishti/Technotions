from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from blog.models import Categories, Post, User
def index(request):
    categories = GetCategories()
    return render(request,'blogtemplates/header.html',
                  {'categories': categories})
  
def posts (request):

  query = request.GET.get("q")
  category = request.GET.get("c")
  user = request.GET.get("u")
  query_list = GetPosts()
  if category:
    query_list = query_list.filter(categories=GetCategories().filter(name=category))
  if user:
    query_list = query_list.filter(user = GetUsers().filter(first_name = user))
  if query:
    query_list = query_list.filter(
      Q(title__icontains=query) |
      Q(body__icontains=query)
      ).distinct()
  paginator = Paginator(query_list, 3)
  page = request.GET.get('page')
  try:
     posts = paginator.page(page)
  except PageNotAnInteger:
      posts = paginator.page(1)
  except EmptyPage:
        posts = paginator.page(paginator.num_pages)
  
  return render(request, 'blogtemplates/blog.html', {'categories': GetCategories(),'posts': posts})

def about(request):
  return render(request, 'blogtemplates/under_construction.html',{'categories': GetCategories()})

def authers(request):
  return render(request, 'blogtemplates/under_construction.html',{'categories': GetCategories()})
def contact(request):
  return render(request, 'blogtemplates/under_construction.html',{'categories': GetCategories()})

def get_categories(request):
 #   categories = json.dumps(Categories.objects.all())    
  #  return HttpResponse(categories)
  data = serializers.serialize('json', Categories.objects.all())
  return HttpResponse(data, content_type="application/json")

def GetCategories():
  return Categories.objects.all()

def GetUsers():
  return User.objects.all()

def GetPosts():
  return Post.objects.all().order_by("-created")

			