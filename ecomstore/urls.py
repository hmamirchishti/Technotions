from django.urls import urls, include
from . import views

urlpatterns =[
    #Todo Need to put views
    url(r'^$',views.index),
    url(r'^category/(?P<category_slug>[-\w]+>)/$',views.category),
    url(r'^product/(?P<product_slug>[-\w]+)/$',views.product)
]