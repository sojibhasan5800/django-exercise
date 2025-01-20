
from django.urls import path
from .views import homepage,aboutpage

urlpatterns = [
  path('',homepage),
  path('about/',aboutpage,name='about_from')
]
