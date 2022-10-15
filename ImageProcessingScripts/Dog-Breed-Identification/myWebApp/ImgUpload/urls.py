# from django.conf.urls import url
from django.contrib import admin
from django.urls import include ,re_path
from django.urls.conf import include
from . import views

urlpatterns = [
    
    re_path(r'^$', views.home, name='home'),
    re_path(r'imageprocess', views.imageprocess , name='imageprocess')
]
