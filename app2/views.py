from django.shortcuts import render


# Create your views here.

def child(request):
    return render(request,"child.html")

def home(request):
    return render(request,"app2/home.html")

def sample(request):
    return render(request,"app2/sample.html")