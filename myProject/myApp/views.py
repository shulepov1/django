import hashlib
from django.shortcuts import render, redirect, get_object_or_404
from myApp.models import Team, Player, Game, Stat, Award, Note
from myApp.filters import GameFilter
from myApp.forms import CreateUserForm, GameForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

def is_player(user):
    return user.groups.filter(name__in=['admin','player']).exists()

def homePage(request):
    notes = Note.objects.order_by('?')[:10]
    context = {'is_homepage': True, 'notes': notes}
    return render(request, 'pages/homepage.html', context)

def show_player_info(request):
    context = {}
    players = Player.objects.all()
    context['players'] = players
    return render(request, 'pages/players.html', context)

def show_awards(request):
    selected_award = None
    if request.method == 'POST':
        selected_award = request.POST.get('selected_award')
    if selected_award:
        awards = Award.objects.filter(name=selected_award)
        return render(request, 'pages/awards.html', {'awards': awards})
    return render(request, 'pages/awards.html')

def get_player_stats(request, player_id):
    try:
        player = Player.objects.filter(id=player_id).values('name','team', 'position', 'jersey_number', 'bio')[0]
        awards = list(Award.objects.filter(players__name__in=[player['name']]).values('name','year'))
        player_stats = list(Stat.objects.filter(player_id = player_id).values('game', 'points', 'rebounds', 'assists'))
        for stat in player_stats:
            game_id = stat['game']
            stat['game_info'] = list(Game.objects.filter(id=game_id).order_by('date').values('date','home_team','away_team','home_team_score', 'away_team_score'))
            for field in stat['game_info'][0]:
                if field == 'home_team' or field == 'away_team':
                    team_id = stat['game_info'][0][field]
                    stat['game_info'][0][field] = Team.objects.filter(id=team_id)[0].name
    except IndexError:
        return JsonResponse({'error': 'Player stats not found'}, status=404)
    
    return JsonResponse({'player': player, 'stats': player_stats, 'awards': awards})

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
    return render(request, 'pages/games.html', context)

def game_delete(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    game.delete()
    return redirect('games')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Successfully created account for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'auth/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        messages.info(request, 'Username or Password is incorrect')
        
    context={}
    return render(request, 'auth/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
