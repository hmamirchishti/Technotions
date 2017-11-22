from django.db import models
from markdownx.models import MarkdownxField


class User(models.Model):
        username = models.CharField(max_length=20)
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        img_url = models.CharField(max_length=300)
        email = models.EmailField()
        twitter = models.CharField(max_length=300)
        google_plus = models.CharField(max_length=300)
        
        facebook = models.CharField(max_length=300)
        created = models.DateTimeField(auto_now_add= True)
        modified = models.DateTimeField(auto_now= True)
        
        def __str__ (self):
            return self.first_name

class EntryQuerySet(models.QuerySet):
    def Published(self):
        return self.filter(published = True)
class Categories(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique = True)
    published = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add= True)
    modified = models.DateTimeField(auto_now=True)    
    objects = EntryQuerySet.as_manager()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ManyToManyField(Categories)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/blog/posts/%s" %(self.id) 

    class meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entry"
        ordering = ["-created"]
        
