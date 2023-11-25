import hashlib
from django.shortcuts import render, redirect
from myApp.models import Player, Game, Stat, Team
from myApp.filters import GameFilter
from myApp.forms import CreateUserForm, GameForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .models import Stat
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.views import generic
from django.shortcuts import get_object_or_404, redirect



def is_player(user):
    return user.groups.filter(name__in=['admin','player']).exists()

# @login_required(login_url='login')
def homePage(request):
    context = {'is_homepage': True}
    return render(request, 'homepage.html', context)

# @login_required(login_url='login')
def show_player_info(request):
    context = {}
    # user = request.user
    # players = Player.objects.filter(id_user_id=user.id)
    players = Player.objects.all()
    stats = Stat.objects.all()
    context['players'] = players
    context['stats'] = stats
    # for player in players:
    #     player.hash = hashlib.md5(player.name.encode('utf-8')).hexdigest()
    return render(request, 'players.html', context)

def get_player_stats(request, player_id):
    try:
        player = Player.objects.filter(id=player_id).values('name','team', 'position', 'jersey_number', 'bio')[0]
        player_stats = list(Stat.objects.filter(player_id = player_id).values('game', 'points', 'rebounds', 'assists'))
        for stat in player_stats:
            game_id = stat['game']
            print(game_id)
            stat['game_info'] = list(Game.objects.filter(id=game_id).order_by('date').values('date','home_team','away_team','home_team_score', 'away_team_score'))
            for field in stat['game_info'][0]:
                if field == 'home_team' or field == 'away_team':
                    team_id = stat['game_info'][0][field]
                    stat['game_info'][0][field] = Team.objects.filter(id=team_id)[0].name
    except IndexError:
        return JsonResponse({'error': 'Player stats not found'}, status=404)
    
    return JsonResponse({'player': player, 'stats': player_stats})

# @login_required(login_url='login')
def show_games(request):
    context = {}
    games = Game.objects.all().order_by('date')
    game_filter = GameFilter(request.GET, queryset=games)

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
    context['filter'] = game_filter
    return render(request, 'games.html', context)

def game_delete(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    game.delete()
    return redirect('games')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
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
            return redirect('home')
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
