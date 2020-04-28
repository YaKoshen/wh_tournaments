from django.contrib import admin

from .models import Player, Tournament, Organizer

class PlayerList(admin.ModelAdmin):
    filter_horizontal = ('players',)

admin.site.register(Player)
admin.site.register(Tournament, PlayerList)
admin.site.register(Organizer)
