from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User


def register(request):
    if request.user.is_authenticated:
        return redirect('index')


    if request.method == 'POST':
        fullname = request.POST['fullname']
        username = request.POST['username'].lower()
        email = request.POST['email'].lower()
        password = request.POST['password']

        if len(fullname) < 5 or len(username) < 3 or len(email) < 5 or len(password) < 5:
            messages.error(request, 'Invaild Form')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'username already exist')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exist')
            return redirect('register')

        user = User.objects.create_user(
            first_name=fullname,
            username=username,
            email=email,
            password=password
        )
        user.save()
        messages.success(request, 'Account Created')
        return redirect('login')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('index')


    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')
        
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if not request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logged Out')
    return redirect('index')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'accounts/profile.html')