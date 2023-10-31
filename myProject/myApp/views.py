from django.shortcuts import render, redirect
from myApp.models import Player, Game
from myApp.forms import CreateUserForm, GameForm
import hashlib
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def homePage(request):
    context = {'is_homepage': True}
    return render(request, 'homepage.html', context)

@login_required(login_url='login')
def show_player_info(request):
    context = {}
    # user = request.user
    # players = Player.objects.filter(id_user_id=user.id)
    players = Player.objects.all()
    context['players'] = players
    for player in players:
        player.hash = hashlib.md5(player.name.encode('utf-8')).hexdigest()
    
    return render(request, 'playerinfo.html', context)

@login_required(login_url='login')
def show_games(request):
    context = {}
    games = Game.objects.all()

    if request.method == "POST":
            form = GameForm(request.POST)
            if form.is_valid():
                form.save()
                form = GameForm()
                return redirect('games')
    else:
        form = GameForm()

    context['games'] = games
    context['form'] = form
    return render(request, 'games.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('players')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Successfully created account for ' + username)
                
                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
            return redirect('players')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context={}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
