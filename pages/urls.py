from django.urls import path
from . import views

urlpatterns = [

   path('', views.index, name='index'),
   path('posts/', views.allPosts, name='allposts'),
   path('post/<slug>', views.showPost, name='showpost'),
   path('about/', views.about, name='about'),
   path('services/', views.services, name='services'),



]
