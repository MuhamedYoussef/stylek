from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def register(request):
    if request.user.is_authenticated:
        return redirect('index')


    if request.method == 'POST':
        first = request.POST['first']
        last = request.POST['last']
        email = request.POST['email'].lower()
        username = request.POST['username'].lower()
        password = request.POST['password']

        if len(first) < 3 or len(last) < 3 or len(email) < 8 or len(username) < 3 or len(password) < 5:
            messages.error(request, 'Invalid Form!')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')

        user = User.objects.create_user(
            first_name=first,
            last_name=last,
            email=email,
            username=username,
            password=password,
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
        email = request.POST['email'].lower()
        password = request.POST['password']

        attempt = User.objects.filter(email=email).first()
        if not attempt:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

        username = attempt.username
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

@login_required
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logged Out')
    return redirect('index')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def edit(request):
    if request.method == 'POST':
        first = request.POST['first']
        last = request.POST['last']
        email = request.POST['email']
        username = request.POST['username']
        bio = request.POST['bio']
        image = request.FILES.get('img', False)


        if len(first) < 3 or len(last) < 3 or len(email) < 8 or len(username) < 3:
            messages.error(request, 'Invalid Form!')
            return redirect('edit')

        if User.objects.filter(username=username.lower()).exclude(id=request.user.id).exists():
            messages.error(request, 'Username already taken')
            return redirect('edit')

        if User.objects.filter(email=email.lower()).exclude(id=request.user.id).exists():
            messages.error(request, 'Email already exists')
            return redirect('edit')

        request.user.first_name = first
        request.user.last_name = last
        request.user.email = email.lower()
        request.user.username = username.lower()
        request.user.profile.bio = bio
        if image:
            request.user.profile.image = image

        request.user.save()
        messages.info(request, 'Profile updated')
        return redirect('profile')
    else:
        return render(request, 'accounts/edit.html')
