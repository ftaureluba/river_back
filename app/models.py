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


class ShootingModel(models.Model):
    player = models.ForeignKey(JugadorModel, on_delete=models.CASCADE)
    goals = models.IntegerField()
    shotsTotal= models.IntegerField()
    shotsOnTarget= models.IntegerField()
    percentShotsOnTarget = models.FloatField()
    shotsPerNinety = models.FloatField()
    shotsOnTargetPerNinety = models.FloatField()
    goalsPerShot = models.FloatField()
    goalsPerShotOnTarget = models.FloatField()
    averageShotDistance = models.FloatField()
    shotFromFreekicks= models.IntegerField()
    penaltyKicks= models.IntegerField()
    penaltyKicksAttempted= models.IntegerField()
    expectedGoals = models.FloatField()
    nonPenaltyExpectedGoals = models.FloatField()
    nonPenaltyExpectedGoalsPerShot = models.FloatField()
    goalsMinusExpectedGoals = models.FloatField()
    nonPenaltyGoalsMinusNonPenaltyExpectedGoals = models.FloatField()


class GoalkeeperStats(models.Model):
    player = models.ForeignKey(JugadorModel, on_delete=models.CASCADE)
    goalsAgainst = models.IntegerField()  # 'GA' - number of goals conceded (int)
    penaltiesAgainst = models.IntegerField()  # 'PKA' - penalties against (int)
    freeKicksAgainst = models.IntegerField()  # 'FK' - free kicks conceded (int)
    cornerKicksAgainst = models.IntegerField()  # 'CK' - corner kicks conceded (int)
    ownGoals = models.IntegerField()  # 'OG' - own goals (int)

    postShotExpectedGoals = models.FloatField()  # 'PSxG' - expected goals after shots (float)
    psxgPerShotOnTarget = models.FloatField()  # 'PSxG/SoT' - expected goals per shot on target (float)
    psxgGoalDifference = models.FloatField()  # 'PSxG+/-' - post-shot xG goal difference (float)
    psxgPer90 = models.FloatField()  # '/90' - PSxG per 90 minutes (float)
    passesCompleted = models.IntegerField()  # 'Cmp' - completed passes (int)
    passesAttempted = models.IntegerField()  # 'Att' - attempted passes (int)
    passCompletionPercentage = models.FloatField()  # 'Cmp%' - pass completion rate (float)
    
    goalkeeperPassesAttempted = models.IntegerField()  # 'Att (GK)' - passes attempted by the GK (int)
    throwsAttempted = models.IntegerField()  # 'Thr' - throws attempted (int)
    launchPassesPercentage = models.FloatField()  # 'Launch%' - percentage of passes that were launched (float)
    launchAvgLength = models.FloatField()  # 'AvgLen' - average length of launched passes (float)
    
    goalKicksAttemptedOther = models.IntegerField()  # 'Att' - passes attempted (non-GK specific, int)
    goalKicksLaunchPercentage = models.FloatField()  # 'Launch%' - percentage of long passes (float)
    goalKicksAvgLength = models.FloatField()  # 'AvgLen' - average length of long passes (float)
    
    crossesFaced = models.IntegerField()  # 'Opp' - number of shots faced (int)
    crossesStopped = models.IntegerField()  # 'Stp' - number of saves (int)
    crossesStoppedPercentage = models.FloatField()  # 'Stp%' - save percentage (float)
    
    sweeperActions = models.IntegerField()  # '#OPA' - number of sweeper actions (int)
    sweeperActionsPer90 = models.FloatField()  # '#OPA/90' - sweeper actions per 90 minutes (float)
    avgDistanceOfSweeperActions = models.FloatField()  # 'AvgDist' - average distance of sweeper actions (float)


class Passing(models.Model):
    player = models.ForeignKey(JugadorModel, on_delete=models.CASCADE)
    completed = models.IntegerField()
    attempted = models.IntegerField()
    completedPercentage = models.FloatField()
    totalDistance = models.IntegerField()
    totalProgressiveDistance = models.IntegerField()
    shortCompleted = models.IntegerField()
    shortAttempted = models.IntegerField()
    shortCompletedPercentage  = models.FloatField()
    mediumCompleted = models.IntegerField()
    mediumAttempted = models.IntegerField()
    mediumCompletedPercentage = models.FloatField()
    longCompleted = models.IntegerField()
    longAttempted = models.IntegerField()
    longCompletedPercentage =models.FloatField()
    assists = models.IntegerField()
    expectedAssistedGoals = models.FloatField()
    expectedAssists = models.FloatField()
    assistsMinusExpectedGoalsAssisted = models.FloatField()
    keyPasses = models.IntegerField()
    passesIntoTheFinalThird = models.IntegerField()
    passesIntoPenaltyArea = models.IntegerField()
    crossesIntoPenaltyArea = models.IntegerField()
    progressivePasses = models.IntegerField()


class PassTypes(models.Model):
    player = models.ForeignKey(JugadorModel, on_delete=models.CASCADE)
    passesAttempted = models.IntegerField()
    livePasses = models.IntegerField()
    deadPasses = models.IntegerField()
    freeKicks = models.IntegerField()
    throughBalls = models.IntegerField()
    switches = models.IntegerField()
    crosses = models.IntegerField()
    throwIns = models.IntegerField()
    corners = models.IntegerField()
    cornersIn = models.IntegerField()
    cornersOut =models.IntegerField()
    cornersStraight = models.IntegerField()
    passesCompleted = models.IntegerField()
    passesOffside = models.IntegerField()
    passesBlocked = models.IntegerField()

class GoalAndShotCreation(models.Model): 
    player = models.ForeignKey(JugadorModel, on_delete=models.CASCADE)
    shotCreatiingAction = models.IntegerField()
    shotCreatiingActionPerNinety = models.FloatField()
    liveSCA = models.IntegerField()
    deadSCA = models.IntegerField()
    takeOnSCA = models.IntegerField()
    shotSCA = models.IntegerField()
    fouldDrawnSCA = models.IntegerField()
    defensiveSCA = models.IntegerField()
    goalCreatingAction = models.IntegerField()
    goalCreatingActionPerNinety = models.FloatField()
    liveGCA =models.IntegerField()
    deadGCA = models.IntegerField()
    takeOnGCA =models.IntegerField()
    shotGCA = models.IntegerField()
    fouldDrawnGCA = models.IntegerField()
    defensiveGCA = models.IntegerField()


class DefensiveActions(models.Model):
    player = models.ForeignKey(JugadorModel, on_delete=models.CASCADE)
    tackles = models.IntegerField()
    tacklesWon = models.IntegerField()
    tacklesDefensiveThird = models.IntegerField()
    tacklesMiddleThird = models.IntegerField()
    tacklesAttackingThird = models.IntegerField()
    dribblersTackled = models.IntegerField()
    dribblesChallenged = models.IntegerField()
    dribblersTackledPercentage = models.FloatField()
    challengesLost = models.IntegerField()
    blocks = models.IntegerField()
    shotsBlocked = models.IntegerField()
    passesBlocked = models.IntegerField()
    interceptions = models.IntegerField()
    tacklesPlusInterceptions = models.IntegerField()
    clearances = models.IntegerField()
    errors = models.IntegerField()

    