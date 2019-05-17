from django.contrib import admin
from django.urls import path, include
from .import views
#from django.conf.urls import patterns, include, urls
#from blog.views import PostsListView, PostDetailView

#admin.autodiscover()

urlpatterns = [
    path('', views.home, name = 'home'),
    path('<int:id>/', views.single, name='single'),


]
