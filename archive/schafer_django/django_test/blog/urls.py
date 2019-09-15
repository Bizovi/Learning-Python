from django.contrib import admin
from django.urls import path
from . import views # from current directory

# urls.py in site tells website which urls open blog app

urlpatterns = [
    path('admin/', admin.site.urls),
    # as /blog/ was processed need only empty string
    # have '', have a pattern that matches '', handled by views.home
    path('', views.home, name='blog-home'),
    # no need to include below into django_test
    path('about/', views.about, name='blog-about'),
]
