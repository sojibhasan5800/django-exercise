from django.urls import path,include
from .views import postpage
urlpatterns = [
 path('page/',postpage,name="post_page")
]