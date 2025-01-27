from django.shortcuts import render,redirect
from .forms import post_form
# Create your views here.
def postpage(request):
   if request.method == 'POST':
         post_forms =  post_form(request.POST)
         if post_forms.is_valid():
            post_forms.save()
            return redirect("post_page")
              
   else:
      post_forms =  post_form()
      return render(request,'add_post.html',{'form':post_forms})