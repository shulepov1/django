import datetime
from django import forms
from django.contrib.auth.models import User
from myApp.models import Game, Team, Player, Award
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.core.exceptions import ValidationError


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class GameForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(datetime.date.today().year, 1900, -1))
    )
    class Meta:
        model = Game
        fields = ['home_team', 'away_team', 'date', 'home_team_score', 'away_team_score']
    def clean(self):
        cleaned_data = super().clean()
        home_team = cleaned_data.get('home_team')
        away_team = cleaned_data.get('away_team')
        home_team_score = cleaned_data.get('home_team_score')
        away_team_score = cleaned_data.get('away_team_score')

        if home_team == away_team:
            raise ValidationError("teams cannot be the same.")
        if home_team_score == away_team_score:
            raise ValidationError("scores cannot be the same.")

        return cleaned_data

class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ['name', 'year', 'players']
    
