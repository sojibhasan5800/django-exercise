from django.shortcuts import render
from posts.models import post
def homepage(request):
    data = post.objects.all() 
    for i in data:
        print(i.title)
        for j in i.catagori.all():
            print(j) 
    return render(request,'home.html',{'data':data})