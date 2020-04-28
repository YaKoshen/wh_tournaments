from django.db import models

class TournametTypes:
    SOLO = 'solo'

class ParingList:
    def __init__(self, players):
        self.players = players
        pass




class Player(models.Model):
    nick = models.CharField(max_length=125, unique=True)

    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)

    raiting = models.IntegerField(default=1600)

    create_time = models.DateTimeField(auto_now=True, editable=False)
    baned = models.BooleanField(default=False)

    def __str__(self):
        return self.nick

class Organizer(models.Model):
    name = models.CharField(max_length=125, unique=True)
    text = models.CharField(max_length=500)

    create_time = models.DateTimeField(auto_now=True, editable=False)
    baned = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Tournament(models.Model):
    name = models.CharField(max_length=125)
    title = models.CharField(max_length=125)
    text = models.CharField(max_length=500)
    link = models.CharField(max_length=500)

    date = models.DateTimeField()
    is_visible = models.BooleanField(default=False)
    tournament_type = models.CharField(default=TournametTypes.SOLO, max_length=10)
    points = models.IntegerField(default=1000)
    tours = models.IntegerField(default=3)

    orginizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return f'{self.name} [ {self.date} ]'

    def get_first_parings(self):
        for player in self.players.order_by('-raiting').all():
            print(player, player.raiting)



        return None
