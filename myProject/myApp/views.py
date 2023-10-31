from django.shortcuts import render
from myApp.models import Player
import hashlib
# Create your views here.

def show_player_info(request):
    user = request.user
    players = Player.objects.filter(id_user_id=user.id)

    for player in players:
        player.hash = hashlib.md5(player.name.encode('utf-8')).hexdigest()
    
    return render(request, 'playerinfo.html', {'players': players})