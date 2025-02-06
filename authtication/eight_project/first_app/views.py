from django.shortcuts import render
from .forms import registerform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def homepage(request):
    data = registerform()
    return render(request,'home.html',{'form':data})

def singuppage(request):
    data = registerform()
    if request.method == 'POST':
        data = registerform(request.POST)
        if data.is_valid():
            messages.success(request,'Account created successfully')
            data.save()
            print(data.cleaned_data)
    else:
        data = registerform()
    return render(request,'signup.html',{'form':data})

def loginpage(request):
    if request.method == 'POST':
        pass


    

