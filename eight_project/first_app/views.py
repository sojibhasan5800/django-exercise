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
    if not request.user.is_authenticated:

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
    else:
        return redirect('signup_page')

def loginpage(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                user_password = form.cleaned_data['password']
                user = authenticate(username = name, password=user_password)
                if user is not None:
                    login(request,user)
                    return redirect('profile_page')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        return redirect('profile_page')



def logoutpage(request):
    logout(request)
    return redirect('login_page')


def profilepage(request):
    if request.user.is_authenticated:
       return render(request,'profile.html',{'user':request.user})  
    else:
        return redirect('login_page')




    

