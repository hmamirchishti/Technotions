from django.shortcuts import render
def index(request):
    posts = Post.objects.all()
    return render_to_response('blogtemplates/blog.html',
                  {'posts': posts},
                  context_instance = RequestContext(request))
def get_categories(request):
    categories = json.dumps(Categories.objects.all())    
    return HttpResponse(categories)