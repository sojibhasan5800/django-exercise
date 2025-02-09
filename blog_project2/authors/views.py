from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def registerpage(request):
    
     if request.method == 'POST':
         register_form = RegistrationForm(request.POST)
         if register_form.is_valid():
             register_form.save()
             messages.success(request,'Account Created Successfully')
             return redirect('register_page')
     else:
         
         register_form = RegistrationForm()
     return render(request,'register.html',{'form': register_form , 'type':'Register'})


def loginpage(request):
     
     
    if request.method == 'POST':
          form = AuthenticationForm(request, request.POST)
          if form.is_valid():
              user_name = form.cleaned_data['username']
              user_pass = form.cleaned_data['password']
              user = authenticate(username=user_name, password=user_pass)
              if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('register_page')
              else:
                messages.warning(request, 'Login informtion incorrect')
                return redirect('register_page')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form' : form, 'type' : 'Login'})
                
                
    
    

    



   
              
     
