# Generated by Django 5.0.7 on 2024-09-07 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_jugadormodel_minutesplayed'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefensiveActions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tackles', models.IntegerField()),
                ('tacklesWon', models.IntegerField()),
                ('tacklesDefensiveThird', models.IntegerField()),
                ('tacklesMiddleThird', models.IntegerField()),
                ('tacklesAttackingThird', models.IntegerField()),
                ('dribblersTackled', models.IntegerField()),
                ('dribblesChallenged', models.IntegerField()),
                ('dribblersTackledPercentage', models.FloatField()),
                ('challengesLost', models.IntegerField()),
                ('blocks', models.IntegerField()),
                ('shotsBlocked', models.IntegerField()),
                ('passesBlocked', models.IntegerField()),
                ('interceptions', models.IntegerField()),
                ('tacklesPlusInterceptions', models.IntegerField()),
                ('clearances', models.IntegerField()),
                ('errors', models.IntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.jugadormodel')),
            ],
        ),
        migrations.CreateModel(
            name='GoalAndShotCreation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shotCreatiingAction', models.IntegerField()),
                ('shotCreatiingActionPerNinety', models.FloatField()),
                ('liveSCA', models.IntegerField()),
                ('deadSCA', models.IntegerField()),
                ('takeOnSCA', models.IntegerField()),
                ('shotSCA', models.IntegerField()),
                ('fouldDrawnSCA', models.IntegerField()),
                ('defensiveSCA', models.IntegerField()),
                ('goalCreatingAction', models.IntegerField()),
                ('goalCreatingActionPerNinety', models.FloatField()),
                ('liveGCA', models.IntegerField()),
                ('deadGCA', models.IntegerField()),
                ('takeOnGCA', models.IntegerField()),
                ('shotGCA', models.IntegerField()),
                ('fouldDrawnGCA', models.IntegerField()),
                ('defensiveGCA', models.IntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.jugadormodel')),
            ],
        ),
        migrations.CreateModel(
            name='GoalkeeperStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goalsAgainst', models.IntegerField()),
                ('penaltiesAgainst', models.IntegerField()),
                ('freeKicksAgainst', models.IntegerField()),
                ('cornerKicksAgainst', models.IntegerField()),
                ('ownGoals', models.IntegerField()),
                ('postShotExpectedGoals', models.FloatField()),
                ('psxgPerShotOnTarget', models.FloatField()),
                ('psxgGoalDifference', models.FloatField()),
                ('psxgPer90', models.FloatField()),
                ('passesCompleted', models.IntegerField()),
                ('passesAttempted', models.IntegerField()),
                ('passCompletionPercentage', models.FloatField()),
                ('goalkeeperPassesAttempted', models.IntegerField()),
                ('throwsAttempted', models.IntegerField()),
                ('launchPassesPercentage', models.FloatField()),
                ('launchAvgLength', models.FloatField()),
                ('goalKicksAttemptedOther', models.IntegerField()),
                ('goalKicksLaunchPercentage', models.FloatField()),
                ('goalKicksAvgLength', models.FloatField()),
                ('crossesFaced', models.IntegerField()),
                ('crossesStopped', models.IntegerField()),
                ('crossesStoppedPercentage', models.FloatField()),
                ('sweeperActions', models.IntegerField()),
                ('sweeperActionsPer90', models.FloatField()),
                ('avgDistanceOfSweeperActions', models.FloatField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.jugadormodel')),
            ],
        ),
        migrations.CreateModel(
            name='Passing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.IntegerField()),
                ('attempted', models.IntegerField()),
                ('completedPercentage', models.FloatField()),
                ('totalDistance', models.IntegerField()),
                ('totalProgressiveDistance', models.IntegerField()),
                ('shortCompleted', models.IntegerField()),
                ('shortAttempted', models.IntegerField()),
                ('shortCompletedPercentage', models.FloatField()),
                ('mediumCompleted', models.IntegerField()),
                ('mediumAttempted', models.IntegerField()),
                ('mediumCompletedPercentage', models.FloatField()),
                ('longCompleted', models.IntegerField()),
                ('longAttempted', models.IntegerField()),
                ('longCompletedPercentage', models.FloatField()),
                ('assists', models.IntegerField()),
                ('expectedAssistedGoals', models.FloatField()),
                ('expectedAssists', models.FloatField()),
                ('assistsMinusExpectedGoalsAssisted', models.FloatField()),
                ('keyPasses', models.IntegerField()),
                ('passesIntoTheFinalThird', models.IntegerField()),
                ('passesIntoPenaltyArea', models.IntegerField()),
                ('crossesIntoPenaltyArea', models.IntegerField()),
                ('progressivePasses', models.IntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.jugadormodel')),
            ],
        ),
        migrations.CreateModel(
            name='PassTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passesAttempted', models.IntegerField()),
                ('livePasses', models.IntegerField()),
                ('deadPasses', models.IntegerField()),
                ('freeKicks', models.IntegerField()),
                ('throughBalls', models.IntegerField()),
                ('switches', models.IntegerField()),
                ('crosses', models.IntegerField()),
                ('throwIns', models.IntegerField()),
                ('corners', models.IntegerField()),
                ('cornersIn', models.IntegerField()),
                ('cornersOut', models.IntegerField()),
                ('cornersStraight', models.IntegerField()),
                ('passesCompleted', models.IntegerField()),
                ('passesOffside', models.IntegerField()),
                ('passesBlocked', models.IntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.jugadormodel')),
            ],
        ),
        migrations.CreateModel(
            name='ShootingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals', models.IntegerField()),
                ('shotsTotal', models.IntegerField()),
                ('shotsOnTarget', models.IntegerField()),
                ('percentShotsOnTarget', models.FloatField()),
                ('shotsPerNinety', models.FloatField()),
                ('shotsOnTargetPerNinety', models.FloatField()),
                ('goalsPerShot', models.FloatField()),
                ('goalsPerShotOnTarget', models.FloatField()),
                ('averageShotDistance', models.FloatField()),
                ('shotFromFreekicks', models.IntegerField()),
                ('penaltyKicks', models.IntegerField()),
                ('penaltyKicksAttempted', models.IntegerField()),
                ('expectedGoals', models.FloatField()),
                ('nonPenaltyExpectedGoals', models.FloatField()),
                ('nonPenaltyExpectedGoalsPerShot', models.FloatField()),
                ('goalsMinusExpectedGoals', models.FloatField()),
                ('nonPenaltyGoalsMinusNonPenaltyExpectedGoals', models.FloatField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.jugadormodel')),
            ],
        ),
    ]
