
from django.urls import path
from .views import homepage,aboutpage,django_from

urlpatterns = [
  path('',homepage),
  path('about/',aboutpage,name='about_from'),
  path('django_from/',django_from,name='django_from')
]
