import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

class Team(models.Model):
    CONFERENCES = (
        ('WEST', 'Western'),
        ('EAST', 'Eastern')
    )
    name = models.CharField(max_length=100, help_text='Введите название команды', null=False, blank=False)
    city = models.CharField(max_length=100, help_text='Из какого города команда', null=False, blank=False)
    conference = models.CharField(max_length=50, help_text='Название конференции', null=False, blank=False, choices=CONFERENCES)
    division = models.CharField(max_length=50, help_text='Название дивизиона', null=True, blank=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id пользователя', help_text='выберите id пользователя', null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"
    
class Player(models.Model):
    POSITIONS = (
        ('PG', 'Point Guard'), # value and human-readable label
        ('SG', 'Shooting Guard'),
        ('SF', 'Small Forward'),
        ('PF', 'Power Forward'),
        ('C', 'Center')
    )
    name = models.CharField(max_length=100, help_text='Введите имя игрока', null=False, blank=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, help_text='Выберите команду', null=False, blank=False)
    position = models.CharField(max_length=50, help_text='Позиция игрока', null=False, blank=False, choices=POSITIONS)
    jersey_number = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(99)], help_text='Введите номер на его майке', null=False, blank=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id пользователя', help_text='выберите id пользователя', null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    def __str__(self):
        return f"({self.team}) {self.name}"
    class Meta:
        unique_together = ('team', 'jersey_number') # jersey number unique только внутри одной Team

class Game(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, help_text='Выберите "хозяев" матча', related_name='home_game', null=False, blank=False)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, help_text='Выберите "гостей" матча', related_name='away_game', null=False, blank=False)
    date = models.DateField(help_text='Введите дату матча', null=False, blank=False)
    home_team_score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(999)], help_text='Введите счет хозяев', null=False, blank=False)
    away_team_score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(999)], help_text='Введите счет гостей', null=False, blank=False)
    def __str__(self):
        return f"({self.date}) {self.home_team} - {self.away_team}"

class Stat(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, help_text='Выберите игрока', null=False, blank=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, help_text='Выберите игру', null=False, blank=False)
    points = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(999)], help_text='Введите количество очков', null=False, blank=False)
    rebounds = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(999)], help_text='Введите количество подборов', null=False, blank=False)
    assists = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(999)], help_text='Введите количество передач', null=False, blank=False)
    def __str__(self):
        return f"{self.player} in {self.game}"
    
class Award(models.Model):
    names = (
        ('MVP', 'Most Valuable Player'), # value and human-readable label
        ('ROY', 'Rookie of the Year'),
        ('DPOY', 'Defensive Player of the Year'),
        ('6MOY', 'Sixth Man of the Year'),
        ('MIP', 'Most Improved Player')
    )
    name = models.CharField(max_length=100, help_text='Название награды', null=False, blank=False, choices=names)
    year = models.IntegerField(choices=[(r, r) for r in range(1900, datetime.date.today().year+1)])
    players = models.ManyToManyField(Player, related_name='players')
    def __str__(self):
        return f"{self.year} {self.name}"
    class Meta:
        unique_together = ('name', 'year')

class Note(models.Model):
    text = models.TextField(max_length=650, null=False, blank=False)
