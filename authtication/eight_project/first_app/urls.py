
from django.urls import path,include
from .views import homepage,singuppage

urlpatterns = [
    path('',homepage,name='home_page'),
    path('singup/',singuppage,name='signup_page')
]