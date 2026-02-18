
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'teams'

class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    team_id = models.CharField(max_length=24, blank=True, null=True)  # Referencia por id
    class Meta:
        db_table = 'users'

class Activity(models.Model):
    user_id = models.CharField(max_length=24, blank=True, null=True)  # Referencia por id
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'activities'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for_ids = models.JSONField(default=list)  # Lista de ids de usuarios
    class Meta:
        db_table = 'workouts'

class Leaderboard(models.Model):
    team_id = models.CharField(max_length=24, blank=True, null=True)  # Referencia por id
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'
