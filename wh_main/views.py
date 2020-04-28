from django.shortcuts import render

from .models import Tournament

def index(request):
    return render(request, 'index.html')

def tournaments_list(request):
    return render(request, 'tournaments.html', {'tournaments': Tournament.objects.all()})

def tournament(request, tournament_id):
    tournament_obj = Tournament.objects.get(id=int(tournament_id))
    print(tournament_obj.get_first_parings())

    return render(request, 'tournament.html', {'tournament': tournament_obj, 'tours': range(1, int(tournament_obj.tours)+1)})
