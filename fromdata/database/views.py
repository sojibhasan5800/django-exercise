from django.shortcuts import render
from .froom import contatfrom
# Create your views here.
def homepage(request):
    
    return render(request,'abc/home.html')
def aboutpage(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email=request.POST.get('email')
        print(email)
        return render(request,'abc/home.html',{'name':name,'email':email})
    return render(request,'abc/about.html')

def django_from(request):
    froms = contatfrom(request.POST)
    if froms.is_valid():
        print(froms.cleaned_data)
    return render(request,'abc/django_from.html',{'from':froms})
