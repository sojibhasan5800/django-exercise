from django.urls import path,include
from .views import catagoripage
urlpatterns = [
 path('page/',catagoripage,name="catagori_page")
]