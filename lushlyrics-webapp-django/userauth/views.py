from base64 import urlsafe_b64encode
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from . tokens import generate_token
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.decorators import login_required

def default(request):
    return render(request, 'player.html')

@login_required
def SignOut(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('login')


def SignIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('default')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not name or not email or not password:
            error_message = 'Please fill in all required fields.'
            return render(request, 'signup.html', {'error_message': error_message})

        user = User.objects.filter(username=name)

        if (user.exists()):
            messages.error(
                request, 'username already taken, please try with another email')
            return redirect('register')
        # Create a new user using the custom UserManager
        try:
            new_user = User.objects.create_user(name, email, password)
            new_user.is_active = False
            new_user.save()

            current_site = get_current_site(request)
            email_subject = "Confirm your email @ Youtify"
            message = render_to_string('email.html', {
                'name': new_user.username,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token': generate_token.make_token(new_user)
            })

            email = EmailMessage(
                email_subject,
                message,
                settings.EMAIL_HOST,
                [new_user.email]
            )

            email.fail_silently = True
            email.send()
            return render(request, 'activate_email.html')
        except ValueError as e:
            error_message = str(e)
            return render(request, 'signup.html', {'error_message': error_message})

    return render(request, 'signup.html')


def sendEmailVerification(name, email, domain, host, token):
    pass


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
    if (myuser is not None and generate_token.check_token(myuser, token)):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        messages.success(request, 'Account successfully activated, please sign in')
        return redirect('default')
    else:
        return render(request, 'activation_failed.html')
