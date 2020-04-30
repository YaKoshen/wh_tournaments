from django.db import models

class TournametTypes:
    SOLO = 'solo'

class Paring:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.points1 = None
        self.points2 = None

    def getPair(self, player):
        if self.player1 == player:
            return self.player2
        elif self.player2 == player:
            return self.player1

        return None

    def getPlayers(self):
        return [self.player1, self.player2]

    def getPoints(self, player=None):
        if not player:
            return [self.points1, self.points2]
        elif self.player1 == player:
            return self.points1
        elif self.player2 == player:
            return self.points2

        return None


class ParingList:
    def __init__(self):
        self.players = []

    def append(self, player1, player2):
        self.players.append(Paring(player1, player2))

    def getAll(self):
        return self.players

class Player(models.Model):
    nick = models.CharField(max_length=125, unique=True)

    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)

    raiting = models.IntegerField(default=1600)

    baned = models.BooleanField(default=False)

    create_time = models.DateTimeField(auto_now=True, editable=False)
    proxibot = models.BooleanField(default=False)

    link = models.CharField(max_length=500)

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

    players_fixed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} [ {self.date} ]'

    def get_first_parings(self):
        err = None
        paring_list = None

        players = self.players.order_by('-raiting').all()
        players_count = len(players)

        for player in players:
            print(player, player.raiting)

        if players_count % 4 == 0:
            group_count = 4
        elif players_count % 2 == 0:
            group_count = 2
        else:
            err = 'Нечётное число игроков'
            return err, None

        groups = []
        group_size = int(players_count / group_count)

        for i in range(0, players_count, group_size):
            groups.append(players[i:i+group_size])

        paring_list = ParingList()
        half_group_count = int(group_count / 2)
        for i in range(half_group_count):
            for j in range(group_size):
                print(groups[i][j], groups[i + half_group_count][j])
                paring_list.append(groups[i][j], groups[i + half_group_count][j])

        return err, paring_list

class PlayerRequest(models.Model):
    nick = models.ForeignKey(Player, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    roster = models.CharField(max_length=500, default='')

    allowed_roster = models.BooleanField(default=False)
    tournament_registered = models.BooleanField(default=False)
