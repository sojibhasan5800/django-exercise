
from django.urls import path,include
from .views import homepage,singuppage,loginpage,logoutpage,profilepage

urlpatterns = [
    path('',homepage,name='home_page'),
    path('singup/',singuppage,name='signup_page'),
    path('login/',loginpage,name='login_page'),
    path('logout/',logoutpage,name='logout_page'),
    path('profile/',profilepage,name='profile_page'),
]