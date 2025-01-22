from django.shortcuts import render

# Create your views here.
from .models import Student
def homepage(request):
    data = Student.objects.all()
    return render(request,'abc/home.html',{'data':data})

