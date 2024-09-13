from rest_framework import serializers
from .models import (
    JugadorModel, ShootingModel, GoalAndShotCreation, GoalkeeperStats,DefensiveActions, Passing, PassTypes, Possession
)


class ShootingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShootingModel
        fields = '__all__'  # Or specify individual fields you need

class GoalAndShotCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalAndShotCreation
        fields = '__all__'

class GoalKeeperStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalkeeperStats
        fields = '__all__'

class DefensiveActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefensiveActions
        fields = '__all__'

class PassingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Passing
        fields = '__all__'

class PassTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassTypes
        fields = '__all__'

class PossessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Possession
        fields = '__all__'

class JugadorSerializer(serializers.ModelSerializer):
    shootingmodel = ShootingModelSerializer(read_only = True)
    goalandshotcreation = GoalAndShotCreationSerializer(read_only = True)
    goalkeeper = GoalKeeperStatsSerializer(read_only = True)
    defensiveactions = DefensiveActionsSerializer(read_only = True)
    passing = PassingSerializer(read_only=True)
    passtypes = PassTypesSerializer(read_only = True)
    possession = PossessionSerializer(read_only=True)
    class Meta:
        model = JugadorModel
        fields = '__all__'
