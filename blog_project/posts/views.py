from django.shortcuts import render,redirect
from .forms import post_form
from posts.models import post
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
   

def editpost(request,id):
   postdata = post.objects.get(pk=id)
   post_forms = post_form(instance=postdata)
   if request.method == 'POST':
         post_forms =  post_form(request.POST,instance=postdata)
         if post_forms.is_valid():
            post_forms.save()
            return redirect("home_page")
         
   return render(request, 'add_post.html', {'form' : post_forms})
              
def deletepost(request,id):
    delete_data = post.objects.get(pk=id)
    delete_data.delete()
    return redirect("home_page")

  