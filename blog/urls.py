from django.shortcuts import render
from django.urls import path
from .import views


urlpatterns = [
    path('', views.blogHome, name="bloghome"),
    path('postComment', views.postComment, name="postComment"),
    path('<str:slug>', views.blogPost, name="blogPost"),
    ]
    