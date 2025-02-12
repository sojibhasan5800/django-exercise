from django.shortcuts import render
from posts.models import post
from catagories.models import catagori
def homepage(request,category_slug=None):
    data = post.objects.all()
    if category_slug is not None:
        category_data =  catagori.objects.get(slug= category_slug)
        data = post.objects.filter()
   
    return render(request,'home.html',{'data':data , 'catagory': catagory_data})