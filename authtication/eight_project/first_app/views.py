from django.shortcuts import render,redirect
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
        user_data = AuthenticationForm(request=request,data = request.POST )
        if user_data.is_valid():
            name =user_data.cleaned_data['username']
            user_pass = user_data.cleaned_data['password']
            user = authenticate(username = name, password =user_pass)
            if user is not None:
                login(request,user)
                return redirect('profile_page')
            else:
                messages.success(request,"username are password incorrect!")
   
    data = AuthenticationForm()
    return render(request,'login.html',{'form':data})




    

