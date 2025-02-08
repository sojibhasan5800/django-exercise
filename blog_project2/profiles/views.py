from django.shortcuts import render,redirect
from .forms import profile_form
from .models import profile
from django.core.exceptions import ValidationError

# Create your views here.
def profilepage(request):
    if request.method == 'POST':
        profile_forms = profile_form(request.POST)
        if profile_forms.is_valid():
           if profile.objects.filter(user = request.user).exists():
            profile_forms.add_error(None, "A profile already exists for this user.")
            print("duplcate")
           else:
            profile_forms.save()
            return redirect('profile_page')
    else:
        profile_forms = profile_form()
        return render(request,'add_profile.html',{'form': profile_forms})
    
    profile_forms = profile_form()
    return render(request, 'add_profile.html', {'form': profile_forms})