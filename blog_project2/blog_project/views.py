from django.shortcuts import render
from posts.models import post
def homepage(request):
    data = post.objects.all() 
   
    return render(request,'home.html',{'data':data})