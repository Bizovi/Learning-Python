from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.listing, name='home-listing'),
    path('list/', views.listing, name='listing'),
]