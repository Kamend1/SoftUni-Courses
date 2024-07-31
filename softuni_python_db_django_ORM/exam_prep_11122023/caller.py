import os
import django

from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import TennisPlayer, Tournament, Match
from django.db.models import Q, Count


# Create queries within functions
def get_tennis_players(search_name=None, search_country=None):
    query_name = Q(full_name__icontains=search_name)
    query_country = Q(country__icontains=search_country)

    if search_name is None and search_country is not None:
        players = TennisPlayer.objects.filter(query_country).order_by('ranking')
    elif search_name is not None and search_country is None:
        players = TennisPlayer.objects.filter(query_name).order_by('ranking')
    elif search_name is not None and search_country is not None:
        players = TennisPlayer.objects.filter(query_name & query_country).order_by('ranking')
    else:
        return ""

    result = []

    for p in players:
        result.append(f"Tennis Player: {p.full_name}, country: {p.country}, ranking: {p.ranking}")

    return '\n'.join(result)


def get_top_tennis_player():
    top_player = TennisPlayer.objects.get_tennis_players_by_wins_count().first()

    if not top_player:
        return ""

    return f"Top Tennis Player: {top_player.full_name} with {top_player.num_wins} wins."


def get_tennis_player_by_matches_count():
    player = TennisPlayer.objects.prefetch_related('matches_players').annotate(num_matches=Count(
        'matches_players'
    )).filter(num_matches__gt=0).order_by('-num_matches', 'ranking').first()

    if not player:
        return ""

    return f"Tennis Player: {player.full_name} with {player.num_matches} matches played."


def get_tournaments_by_surface_type(surface=None):

    if surface is None:
        return ""

    tournaments = Tournament.objects.prefetch_related('matches').filter(
        surface_type__icontains=surface).annotate(num_matches=Count('matches')).order_by('-start_date')

    result = []

    for t in tournaments:
        result.append(f"Tournament: {t.name}, start date: {t.start_date}, matches: {t.num_matches}")

    return '\n'.join(result)


def get_latest_match_info():
    match = Match.objects.order_by('-date_played', '-id').first()

    if not match:
        return ""

    players = [p.full_name for p in match.players.all()]
    winner = match.winner.full_name if match.winner else 'TBA'

    return (f"Latest match played on: {match.date_played}, "
            f"tournament: {match.tournament.name}, "
            f"score: {match.score}, "
            f"players: {players[0]} vs {players[1]}, "
            f"winner: {winner}, "
            f"summary: {match.summary}")


def get_matches_by_tournament(tournament_name=None):

    if tournament_name is None:
        return "No matches found."

    # tournament = Tournament.objects.prefetch_related('matches').filter(name=tournament_name).order_by(
    #     '-matches__date_played'
    # ).first()

    matches = Match.objects.prefetch_related('tournament').filter(tournament__name=tournament_name).order_by(
        '-date_played'
    )

    if not matches.exists():
        return "No matches found."

    result = []

    for match in matches.all():
        result.append(f'Match played on: {match.date_played}, '
                      f'score: {match.score}, '
                      f'winner: {match.winner.full_name if match.winner is not None else "TBA"}')

    return '\n'.join(result)
print(get_matches_by_tournament('Wimbledon'))