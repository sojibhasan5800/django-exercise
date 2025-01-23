from django.urls import path,include
from .views import homepage,deletedata
urlpatterns = [
    path('',homepage),
    path('deleted/<int:roll>/',deletedata,name='delete_student')
]
