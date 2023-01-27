from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from typing import Type
from .models import *
from .forms import *
# from . import forms



def index(request):
    if request.session.get('username', None):
        x = request.session['username']
        return render(request, 'index.html', {"name": x})
    else:
        return redirect('login')

def produitList(request):
    if request.session.get('username', None):
        userId = User.objects.get(
            username=request.session['username'])
        produitList = Produit.objects.all()
        # print(bookingList)
        return render(request, 'produits.html', {"produitList": produitList})
    else:
        return redirect('login')
def clientList(request):
    
    clientList = Client.objects.all()
    return render(request, 'clients.html', {"clientList": clientList})

def foursList(request):
    
    foursList = Fournisseur.objects.all()
    return render(request, 'fournis.html', {"foursList": foursList})

def facturesList(request):

    facturesList = Facture.objects.all()
    return render(request, 'factures.html', {"facturesList": facturesList})


# @login_required(login_url='adminlogin')
def update_fact_view(request,pk):
    fact=models.Facture.objects.get(id=pk)
    factForm=forms.FactForm(instance=fact)
    if request.method=='POST':
        factForm=forms.FactForm(request.POST,request.FILES,instance=fact)
        if factForm.is_valid():
            factForm.save()
            return redirect('facturesList')
    return render(request,'finanance/admin_update_fact.html',{'factForm':factForm})



def logout(request):
    for key in list(request.session.keys()):
        del request.session[key]
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
                request.session['id'] = user.id
                request.session['username'] = username
                return redirect('index')
            else:
                messages.warning(request, "username or password is incorrect")
                redirect('login')
        else:
            messages.warning(request, "account 404")
            redirect('login')
    return render(request, 'login.html', {})
