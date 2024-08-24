from rest_framework import serializers
from .models import (
    TeamModel, LeagueModel, StatisticsModel, 
    PlayerModel
)

class TeamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamModel
        fields = '__all__'

class LeagueModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeagueModel
        fields = '__all__'


class StatisticsModelSerializer(serializers.ModelSerializer):
    team = TeamModelSerializer()
    league = LeagueModelSerializer()


    class Meta:
        model = StatisticsModel
        fields = '__all__'

class PlayerModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PlayerModel
        fields = '__all__'


    
   

