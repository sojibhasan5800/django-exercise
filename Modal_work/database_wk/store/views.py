from django.shortcuts import render,redirect

# Create your views here.
from .models import Student
def homepage(request):
    data = Student.objects.all()
    return render(request,'abc/home.html',{'data':data})
def deletedata(request,roll):
    Student.objects.get(pk = roll).delete()
    
    data = Student.objects.all()
    return render(request,'abc/home.html',{'data':data})

