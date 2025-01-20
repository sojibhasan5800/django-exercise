from django.shortcuts import render

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
