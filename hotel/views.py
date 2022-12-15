from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import User


def index(request):
    if request.session.get('username', None):
        x = request.session['username']
        return render(request, 'index.html', {"name": x})
    else:
        return redirect('login')


def book(request, id):
    if request.session.get('username', None):
        x = request.session['username']
        return render(request, 'index.html', {"name": x})
    else:
        return redirect('login')


def register(request):
    if request.session.get('username', None):
        return redirect('index')
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        if User.objects.filter(username=username) or User.objects.filter(email=email):
            messages.warning(request, "account already exist")
        else:
            password = request.POST['password']
            error = []
            if (len(username) < 3):
                error.append(1)
                messages.warning(
                    request, "Username Field must be greater than 3 character.")
            if (len(password) < 5):
                error.append(1)
                messages.warning(
                    request, "Password Field must be greater than 5 character.")
            if (len(email) == 0):
                error.append(1)
                messages.warning(request, "Email field can't be empty")
            if (len(error) == 0):
                password_hash = make_password(password)
                user = User(username=username,
                            password=password_hash, email=email)
                user.save()
                messages.info(request, "account created successfully")
                redirect('register')
            else:
                redirect('register')
    return render(request, 'register.html', {})


def login(request):
    if request.session.get('username', None):
        return redirect('index')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if not len(username):
            messages.warning(request, "username is empty")
            redirect('login')
        elif not len(password):
            messages.warning(request, "password is empty")
            redirect('login')
        else:
            pass
        if User.objects.filter(username=username):
            user = User.objects.filter(username=username)[0]
            password_hash = user.password
            resp = check_password(password, password_hash)
            if resp == 1:
                request.session['username'] = username
                return redirect('index')
            else:
                messages.warning(request, "username or password is incorrect")
                redirect('login')
        else:
            messages.warning(request, "account 404")
            redirect('login')
    return render(request, 'login.html', {})
