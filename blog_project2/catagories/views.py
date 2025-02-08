from django.shortcuts import render,redirect
from .forms import catagory_form
# Create your views here.
def catagoripage(request):
    if request.method == 'POST':
        catagory_forms = catagory_form(request.POST)
        if catagory_forms.is_valid():
            catagory_forms.save()
            return redirect('catagori_page')
    else:
        catagory_forms = catagory_form()
        return render(request,'add_catagory.html',{'form': catagory_forms})
 
