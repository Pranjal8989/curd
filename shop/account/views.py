from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Remove unused imports
# from django.conf import settings
# from django.shortcuts import redirect

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('inventory')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    
    return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        elif User.objects.filter(username=uname).exists():
            return HttpResponse("Username already exists!")
        elif User.objects.filter(email=email).exists():
            return HttpResponse("Email already registered!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
    
    return render(request, "signup.html")
def Logout(request):
    logout(request)
    return redirect('login')
