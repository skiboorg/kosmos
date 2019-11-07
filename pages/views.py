from django.shortcuts import render
from blog.models import *

def index(request):
    return render(request, 'pages/index.html', locals())

def allPosts(request):
    allPost = BlogPost.objects.filter(is_active=True)
    return render(request, 'pages/posts.html', locals())

def showPost(request,slug):
    post = BlogPost.objects.get(name_slug=slug)
    return render(request, 'pages/post.html', locals())

def about(request):
    return render(request, 'pages/about.html', locals())

def services(request):
    return render(request, 'pages/services.html', locals())