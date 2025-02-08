from django.urls import path,include
from .views import profilepage
urlpatterns = [
 path('page/',profilepage,name="profile_page")
]