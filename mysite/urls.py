"""mysite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from blog import urls as blog
from FirstPageApp import urls as FirstPageApp
from portfolio import urls as Portfolio
from markdownx import urls as markdownx
from django.conf    import settings
from django.conf.urls.static    import static
from ecomstore import urls as ecomstore
urlpatterns = [
    url(r'^',include(FirstPageApp)),
    url(r'^blog/',include(blog)),
    url(r'^ecomstore',include(ecomstore)),
    url(r'^portfolio',include(Portfolio)),
    url(r'^markdownx/', include(markdownx)),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)