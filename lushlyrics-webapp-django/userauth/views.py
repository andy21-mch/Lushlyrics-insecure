from django.shortcuts import redirect, render
from verify_email.email_handler import send_verification_email
from django.contrib.auth.models import User
from django.contrib import messages
def default(request):
    return render('login.html')

def login(request):
   return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not name or not email or not password:
            error_message = 'Please fill in all required fields.'
            return render(request, 'signup.html', {'error_message': error_message})
        
        user = User.objects.filter(username=name)

        if(user.exists()):
            messages.error(request, 'username already taken, please try with another email')
            return redirect('register')
        # Create a new user using the custom UserManager
        try:
            new_user = User.objects.create_user(name, email, password)
            # send_verification_email(request, new_user)
            return render(request, 'login.html')
        except ValueError as e:
            error_message = str(e)
            return render(request, 'signup.html', {'error_message': error_message})
        
    return render(request, 'signup.html')