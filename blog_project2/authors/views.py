from django.shortcuts import render,redirect
from .forms import RegistrationForm,changeuserform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.decorators import login_required

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
                return redirect('profile_page')
              else:
                messages.warning(request, 'Login informtion incorrect')
                return redirect('register_page')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form' : form, 'type' : 'Login'})

@login_required
def profilepage(request):
    return render(request,'profile.html')

@login_required
def edit_profilepage(request):

    if request.method == 'POST':
        profile_form = changeuserform(request.POST , instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Account Updated Successfully')
            return redirect('profile_page')
    else:
        profile_form = changeuserform(instance =request.user)
    return render(request,'edit_profile.html',{'form': profile_form })

def logoutpage(request):
    logout(request)
    return redirect('login_page')


def chngpasspage(request):

    if request.method == 'POST':
        password_cng_form = PasswordChangeForm(request.user , data=request.POST)
        if password_cng_form.is_valid():
            password_cng_form.save()
            update_session_auth_hash(request,password_cng_form.user)
            messages.success(request,'Password Updated Successfully')
            return redirect('profile_page')
    else:       
        password_cng_form = PasswordChangeForm(user=request.user)
    return render(request,'password_chng.html',{'form': password_cng_form })


                
                
    
    

    



   
              
     
