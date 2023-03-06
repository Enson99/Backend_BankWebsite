from django import views
from django.contrib import admin
from django.urls import path
from .views import home,register,login,newpage,success

urlpatterns = [
    path('',home, name='home'),
    path('register.html',register, name='register'),
    path('login.html',login, name='login'),
    path('newpage.html',newpage, name='newpage'), 
]


