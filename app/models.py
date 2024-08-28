from django.db import models

class TeamModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    logo = models.URLField(blank=True, null=True)

class LeagueModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    country = models.CharField(max_length=100,blank=True, null=True)
    logo = models.URLField(blank=True, null=True)
    flag = models.URLField(blank=True, null=True)
    season = models.IntegerField(blank=True, null=True)

class StatisticsModel(models.Model):
    team = models.ForeignKey(TeamModel, on_delete=models.CASCADE,blank=True, null=True)
    league = models.ForeignKey(LeagueModel, on_delete=models.CASCADE,blank=True, null=True)
    statistics = models.JSONField(blank=True, null=True)


class PlayerModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    birth_info = models.JSONField(blank=True, null=True)  # JSON field for birth details
    nationality = models.CharField(max_length=100, blank=True, null=True)
    height = models.CharField(max_length=10, blank=True, null=True)
    weight = models.CharField(max_length=10, blank=True, null=True)
    injured = models.BooleanField(blank=True, null=True)
    photo = models.URLField(blank=True, null=True)
    stats = models.ManyToManyField(StatisticsModel,blank=True, null=True)

'''
class RelevantData(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    partidos =  #titular, suplente ?? 
    rating = models.FloatField(blank=True, null=True) #un int o float
    goles = models.IntegerField(blank=True, null=True)#int
    asistencias =  models.IntegerField(blank=True, null=True)#int
    pases = models.IntegerField(blank=True, null=True)#int
    tackles = models.IntegerField(blank=True, null=True)#int
    duelos = # un porcentaje de ganados / total
    gambetas = #tambien se puede hacer un porcentaje, hay attempts, success y 'past' que no se a que se refiere.'''