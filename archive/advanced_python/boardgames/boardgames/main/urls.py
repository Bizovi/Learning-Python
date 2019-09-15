from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # display hello world to all subdirs
    path('', views.home, name="home"),
    path('crudops/', views.crudops, name='crudops'),
]
