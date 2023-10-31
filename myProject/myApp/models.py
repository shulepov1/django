from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(**kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Team(models.Model):
    def __str__(self):
        return f"{self.city} {self.name}"
    CONFERENCES = (
        ('WEST', 'Western'),
        ('EAST', 'Eastern')
    )
    name = models.CharField(max_length=100, primary_key=True, help_text='Введите название команды', null=False, blank=False)
    city = models.CharField(max_length=100, help_text='Из какого города команда', null=False, blank=False)
    conference = models.CharField(max_length=50, help_text='Название конференции', null=False, blank=False, choices=CONFERENCES)
    division = models.CharField(max_length=50, help_text='Название дивизиона', null=True, blank=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id пользователя', help_text='выберите id пользователя', null=True, blank=True)

class Player(models.Model):
    def __str__(self):
        return f"({self.team}) {self.name}"
    class Meta:
        unique_together = ('team', 'jersey_number') # jersey number unique только внутри одной Team
    POSITIONS = (
        ('PG', 'Point Guard'), # value and human-readable label
        ('SG', 'Shooting Guard'),
        ('SF', 'Small Forward'),
        ('PF', 'Power Forward'),
        ('C', 'Center')
    )
    name = models.CharField(max_length=100, primary_key=True, help_text='Введите имя игрока', null=False, blank=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, help_text='Выберите команду', null=False, blank=False)
    position = models.CharField(max_length=50, help_text='Позиция игрока', null=False, blank=False, choices=POSITIONS)
    jersey_number = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(99)], help_text='Введите номер на его майке', null=False, blank=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id пользователя', help_text='выберите id пользователя', null=True, blank=True)


class Game(models.Model):
    def __str__(self):
        return f"({self.date}) {self.home_team} - {self.away_team}"
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, help_text='Выберите "хозяев" матча', related_name='home_game', null=False, blank=False)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, help_text='Выберите "гостей" матча', related_name='away_game', null=False, blank=False)
    date = models.DateField(help_text='Введите дату матча', null=False, blank=False)
    home_team_score = models.IntegerField(default=0, validators=[MinValueValidator(0)], help_text='Введите счет хозяев', null=False, blank=False)
    away_team_score = models.IntegerField(default=0, validators=[MinValueValidator(0)], help_text='Введите счет гостей', null=False, blank=False)


class Stat(models.Model):
    def __str__(self):
        return f"{self.player} in {self.game}"
    player = models.ForeignKey(Player, on_delete=models.CASCADE, help_text='Выберите игрока', null=False, blank=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, help_text='Выберите игру', null=False, blank=False)
    points = models.IntegerField(default=0, validators=[MinValueValidator(0)], help_text='Введите количество очков', null=False, blank=False)
    rebounds = models.IntegerField(default=0, validators=[MinValueValidator(0)], help_text='Введите количество подборов', null=False, blank=False)
    assists = models.IntegerField(default=0, validators=[MinValueValidator(0)], help_text='Введите количество передач', null=False, blank=False)
