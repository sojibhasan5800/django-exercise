"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import homepage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage,name='home_page'),
    path('catagory/<slug:category_slug>/', homepage,name='catagory_slug_post'),
    path('author/',include('authors.urls')),
    path('catagori/',include('catagories.urls')),
    path('post/',include('posts.urls')),
   
]
