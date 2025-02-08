from django.urls import path,include
from .views import postpage,editpost,deletepost
urlpatterns = [
 path('page/',postpage,name="post_page"),
 path('edit/<int:id>/',editpost,name="edit_page"),
 path('delete/<int:id>/',deletepost,name="delete_page")
]