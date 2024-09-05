from django.db import models


class JugadorModel(models.Model):
    player = models.CharField(max_length=100)
    nation = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.CharField(max_length=100) #aca capaz conviene que sea un int? para hacer comparaciones por edad y demas en vez de un dato estatico? Aunque tambien es mas comodo que sea un string porque son dos numeros: anios y dias.
    matchesPlayed = models.IntegerField()
    starts = models.IntegerField()   
    minutesPlayed = models.FloatField()
    nineties = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    goalsPlusAssists = models.IntegerField()
    goalsMinusPenalties = models.IntegerField()
    penalties = models.IntegerField()
    penaltiesAttempted = models.IntegerField()
    yellowCards = models.IntegerField()
    redCards = models.IntegerField()
    expectedGoals = models.FloatField()
    nonPenaltyExpectedGoals = models.FloatField()
    expectedAssists = models.FloatField()
    nonPenaltyGoalsPlusExpectedAssists = models.FloatField()
    progressiveCarries = models.IntegerField()
    progressivePasses = models.IntegerField()
    progressivePassesReceived = models.IntegerField()
    goalsPerNinety = models.FloatField()
    assistsPerNinety = models.FloatField()
    goalsPlusAssistsPerNinety = models.FloatField()
    goalsMinusPenaltiesPerNinety = models.FloatField()
    goalsPlusAssistsMinusPenaltiesPerNinety = models.FloatField()
    expectedGoalsPerNinety = models.FloatField()
    expectedAssistsPerNinety = models.FloatField()
    expectedGoalsPlusAssistsPerNinety = models.FloatField()
    nonPenaltyExpectedGoalsPerNinety = models.FloatField()
    nonPenaltyGoalsPlusExpectedAssistsPerNinety = models.FloatField()


