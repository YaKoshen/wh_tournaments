from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from wh_main import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('tournament/<str:tournament_id>', views.tournament),
    path('tournaments/', views.tournaments_list),
    path('player/<str:nick>', views.player),
    path('players/', views.players_list)
]
