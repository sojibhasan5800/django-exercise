
from django.urls import path,include
from .views import registerpage,loginpage
urlpatterns = [
 path('register/',registerpage,name="register_page"),
 path('login/',loginpage,name="login_page"),
]