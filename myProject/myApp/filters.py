from django_filters import FilterSet, ModelChoiceFilter
from .models import Team, Game

class GameFilter(FilterSet):
    home_team = ModelChoiceFilter(queryset = Team.objects.all())
    away_team = ModelChoiceFilter(queryset = Team.objects.all())
    class Meta:
        model = Game
        fields = ['home_team', 'away_team']