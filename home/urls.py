from django.shortcuts import render
from django.urls import path
from .import views


urlpatterns = [
    path('test', views.test,name='test'),
    path('',views.home,name='home'),
    path('aboutUs',views.aboutUs,name='aboutUs'),
    path('contact',views.contact,name='contact'),
    path('search', views.search, name="search"),
    path('signup',views.handleSignUp,name='handleSignUp'),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    ]