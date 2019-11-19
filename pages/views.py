from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import *
from .models import *

def index(request):
    return render(request, 'pages/index.html', locals())

def allPosts(request):
    allPost = BlogPost.objects.filter(is_active=True)
    return render(request, 'pages/posts.html', locals())

def showPost(request,slug):
    post = get_object_or_404(BlogPost, name_slug=slug)
    return render(request, 'pages/post.html', locals())

def about(request):
    return render(request, 'pages/about.html', locals())

def services(request):
    return render(request, 'pages/services.html', locals())

def service(request,slug):

    currentService = get_object_or_404(ServiceName, name_slug=slug)
    pageTitle = currentService.page_title
    pageDescription = currentService.page_description
    pageKeywords = currentService.page_keywords
    return render(request, 'pages/services.html', locals())


def robots(request):
    robotsTxt = f"User-agent: *\nDisallow: /admin/\nHost: http://www.buhkosmos174.ru/\nSitemap: http://www.buhkosmos174.ru/sitemap.xml"
    return HttpResponse(robotsTxt, content_type="text/plain")