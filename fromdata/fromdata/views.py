from django.shortcuts import render

def basepage(request):
    return render(request,'base.html')