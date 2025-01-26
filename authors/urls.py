
from django.urls import path,include
from .views import authorpage
urlpatterns = [
 path('page/',authorpage,name="author_page")
]