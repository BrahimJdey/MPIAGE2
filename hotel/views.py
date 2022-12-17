from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import User, Booking


def index(request):
    if request.session.get('username', None):
        x = request.session['username']
        return render(request, 'index.html', {"name": x})
    else:
        return redirect('login')


def book(request):
    if request.session.get('username', None):
        return render(request, 'book.html')
    else:
        return redirect('login')


def booking(request):
    if request.session.get('username', None):
        userId = User.objects.get(
            username=request.session['username'])
        bookingList = Booking.objects.filter(bookedBy=userId)
        print(bookingList)
        return render(request, 'booking.html', {"bookingList": bookingList})
    else:
        return redirect('login')


def bookCancel(request, id):
    if request.session.get('username', None):
        userId = User.objects.get(
            username=request.session['username'])
        try:
            room = Booking.objects.get(id=id, bookedBy=userId)
            room.delete()
            return render(request, 'bookCancel.html', {"id": id})
        except:
            return redirect('booking')
    else:
        return redirect('login')


def bookRoom(request, id):
    if request.session.get('username', None):
        if id in [1, 2, 3]:
            # print(request.POST)
            if request.method == "POST":
                if 'days' in request.POST and 'price' in request.POST:
                    days = int(request.POST['days'])
                    if id == 1:
                        price = 50
                        foodCheck = 100 if 'foodCheck' in request.POST else 0
                        spaCheck = 200 if 'spaCheck' in request.POST else 0
                        gymCheck = 100 if 'gymCheck' in request.POST else 0
                        clubCheck = 50 if 'clubCheck' in request.POST else 0
                        swimmingCheck = 90 if 'swimmingCheck' in request.POST else 0
                        gamesCheck = 50 if 'gamesCheck' in request.POST else 0
                    elif id == 2:
                        price = 100
                        foodCheck = 100 if 'foodCheck' in request.POST else 0
                        spaCheck = 200 if 'spaCheck' in request.POST else 0
                        gymCheck = 100 if 'gymCheck' in request.POST else 0
                        clubCheck = 200 if 'clubCheck' in request.POST else 0
                        swimmingCheck = 100 if 'swimmingCheck' in request.POST else 0
                        gamesCheck = 50 if 'gamesCheck' in request.POST else 0
                    else:
                        price = 500
                        foodCheck = 200 if 'foodCheck' in request.POST else 0
                        spaCheck = 200 if 'spaCheck' in request.POST else 0
                        gymCheck = 200 if 'gymCheck' in request.POST else 0
                        clubCheck = 350 if 'clubCheck' in request.POST else 0
                        swimmingCheck = 150 if 'swimmingCheck' in request.POST else 0
                        gamesCheck = 50 if 'gamesCheck' in request.POST else 0

                    items = {
                        "Days": days * price,
                        "Food": days * foodCheck,
                        "Spa": days * spaCheck,
                        "Gym": days * gymCheck,
                        "Club": days * clubCheck,
                        "Swimming": days * swimmingCheck,
                        "Games": days * gamesCheck,
                    }

                    total = days * (price + foodCheck + spaCheck +
                                    gymCheck + clubCheck + swimmingCheck + gamesCheck)
                    return render(request, 'bookRoom.html', {"id": id, "items": items, "total": total})
                elif request.method == "POST" and 'book' in request.POST and 'Days' in request.POST:
                    print(request.POST)
                    if id == 1:
                        price = 50
                    elif id == 2:
                        price = 100
                    else:
                        price = 500
                    userId = User.objects.get(
                        username=request.session['username'])
                    Days = int(request.POST['Days'])/price
                    Amount = int(request.POST['amount'])
                    Food = True if request.POST['Food'] != '0' else False
                    Spa = True if request.POST['Spa'] != '0' else False
                    Gym = True if request.POST['Gym'] != '0' else False
                    Club = True if request.POST['Club'] != '0' else False
                    Swimming = True if request.POST['Swimming'] != '0' else False
                    Games = True if request.POST['Games'] != '0' else False
                    booking = Booking(days=Days, amount=Amount, food=Food, spa=Spa,
                                      gym=Gym, club=Club, swimming=Swimming, games=Games, bookedBy=userId)
                    booking.save()
                    messages.info(request, "Room booked successfully.")
                    return render(request, 'bookRoom.html', {"id": id})
                else:
                    return render(request, 'bookRoom.html', {"id": id})
            else:
                return render(request, 'bookRoom.html', {"id": id})
        else:
            return redirect('book')
    else:
        return redirect('login')


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
