from django.contrib import admin
from main_app.models import TennisPlayer, Tournament, Match


# Register your models here.
@admin.register(TennisPlayer)
class TennisPlayerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'country', 'ranking', 'is_active']
    list_filter = ['is_active',]
    search_fields = ['full_name', 'country' ]


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'prize_money', 'surface_type', 'start_date']
    search_fields = ['name', 'location']
    list_filter = ['surface_type',]


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['date_played', 'score', 'summary']
    list_filter = ['date_played']
    search_fields = ['tournament__name',]

