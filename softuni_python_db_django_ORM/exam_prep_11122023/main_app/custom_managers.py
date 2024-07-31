from django.db import models
from django.db.models import Count


class TennisPLayerCustomManager(models.Manager):

    def get_tennis_players_by_wins_count(self):
        return self.prefetch_related('match_winner').annotate(num_wins=Count('match_winner')).order_by(
            '-num_wins',
            'full_name')
