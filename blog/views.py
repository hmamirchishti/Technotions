from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import simplejson as json
from blog.models import Categories
def index(request):
    categories = Categories.objects.all()
    return render(request,'blogtemplates/blog.html',
                  {'categories': categories})
def get_categories(request):
 #   categories = json.dumps(Categories.objects.all())    
  #  return HttpResponse(categories)
  data = serializers.serialize('json', Categories.objects.all())
  return HttpResponse(data, content_type="application/json")