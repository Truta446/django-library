from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages

def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']

        if not first_name.strip():
            messages.error(request, 'Name cannot be blank')
            return redirect('register')
        if not last_name.strip():
            messages.error(request, 'Last name cannot be blank')
            return redirect('register')
        if not email.strip():
            messages.error(request, 'Email cannot be blank')
            return redirect('register')
        if password != confirm_password:
            messages.error(request, 'Passwords must match')
            return redirect('register')

        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=f'{first_name.lower()}_{last_name.lower()}',
            password=password
        )

        messages.success(request, 'Successfully registered user!')

        return redirect('login')
    else:
        return render(request, 'users/register.html')

def login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if email == '' or password == '':
            messages.error(request, 'Email and password cannot be blank')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            username = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login successfully!')
                return redirect('index')
            
        messages.error(request, 'User not found')
        return redirect('login')
    else:
        return render(request, 'users/login.html')

def logout(request: HttpRequest) -> HttpResponse:
    auth.logout(request)

    return redirect('index')
