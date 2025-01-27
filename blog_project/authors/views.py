from django.shortcuts import render,redirect
from .forms import author_form
# Create your views here.

def authorpage(request):
     if request.method == 'POST':
          form =  author_form(request.POST)
          if form.is_valid():
               form.save()
               return redirect("author_page")
              
     else:
        form =  author_form()
        return render(request,'add_author.html',{'form':form})
   
              
     
