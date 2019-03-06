from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=128)
    abbreviation = models.CharField(max_length=10)
    captain = models.ForeignKey(User, on_delete=models.CASCADE, related_name='captain', blank=True)
    players = models.ManyToManyField(User, through='PlayersInTeam')

    def __str__(self):
        return '%s' % (self.abbreviation)

class Season(models.Model):
    is_active = models.BooleanField(default=False)
    year = models.CharField(max_length=4, unique=True)
    teams = models.ManyToManyField(Team, blank=True)

    def __str__(self):
        return '%s' % (self.year)

class PlayersInTeam(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('player', 'season')
        # Make sure are players allowed to change team during the season?

class Match(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    match_time = models.DateTimeField()
    home_first_round_score = models.IntegerField()
    home_second_round_score = models.IntegerField()
    away_first_round_score = models.IntegerField()
    away_second_round_score = models.IntegerField()
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    is_validated = models.BooleanField(default=False)

# class ThrowType(models.Model):
#     throw_order_ingame = models.CharField()

class Throw(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    throw_turn = models.CharField(max_length=1)
    # throw_type = models.ForeignKey(ThrowType, on_delete=models.CASCADE)
    score = models.CharField(max_length=2)

# TBD if used
class UserRoles(models.Model):
    ROLES = (
        (1,'Admin'),
        (2,'captain'),
        (3,'player'),
        )
    role = models.CharField(max_length=6,choices=ROLES)

class News(models.Model):
    header = models.TextField()
    date = models.DateTimeField()
    text = models.TextField()
