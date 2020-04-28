from django.shortcuts import render

from .models import Tournament, Player

def index(request):
    return render(request, 'index.html')

def tournament(request, tournament_id):
    tournament_obj = Tournament.objects.get(id=int(tournament_id))
    players = tournament_obj.players.order_by('-raiting').all()
    print(tournament_obj.get_first_parings())

    return render(request, 'tournament.html', {'tournament': tournament_obj, 'tours': range(1, int(tournament_obj.tours)+1), 'players': players})

def tournaments_list(request):
    return render(request, 'tournaments_list.html', {'tournaments': Tournament.objects.all()})

def players_list(request):
    return render(request, 'players_list.html', {'players': Player.objects.order_by('-raiting').all()})

def player(request, nick):
    return render(request, 'player.html', {'player': Player.objects.get(nick=nick)})
