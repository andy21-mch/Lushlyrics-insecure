from django.shortcuts import render

# Create your views here.

def default(request):
    return render('login.html')

def login(request):
   return render(request,'login.html')

def register(request):
    return render(request, 'signup.html')