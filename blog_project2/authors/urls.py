
from django.urls import path,include
from .views import registerpage,loginpage,edit_profilepage,logoutpage,chngpasspage,profilepage
urlpatterns = [
 path('register/',registerpage,name="register_page"),
 path('login/',loginpage,name="login_page"),
 path('edit_profiles/',edit_profilepage,name='edit_profile_page'),
 path('profile/',profilepage,name='profile_page'),
 path('logout/',logoutpage,name='logout_page'),
 path('passwordchange/',chngpasspage,name='chngpass_page'),
]