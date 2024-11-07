from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from .services import getMatchSofascore
from .models import *
from rest_framework import generics

from .serializers import JugadorSerializer, MatchDataSerializer




class JugadorListCreate(generics.ListCreateAPIView):
    queryset = JugadorModel.objects.select_related(
    'shootingmodel', 
    'goalandshotcreation', 
    'goalkeeperstats', 
    'defensiveactions', 
    'passing', 
    'passtypes',
    'possession'
    ).all()
    serializer_class = JugadorSerializer
class MatchStatsAPIView(APIView):

    def get(self, request):
        
        try:
            # Scrape the data from SofaScore
            home_team_df, away_team_df =  getMatchSofascore.data_sofascore()
            
            # Convert the Pandas DataFrame into JSON-like structures
            home_players_data = home_team_df.to_dict(orient='records')
            away_players_data = away_team_df.to_dict(orient='records')

            # Link players to your existing database (pseudo code example)
            for player_data in home_players_data:
                 player_instance = JugadorModel.objects.filter(name=player_data['player']).first()
                 player_data['player_id'] = player_instance.id if player_instance else None
            
            # Serialize the data
            home_team_serialized = MatchDataSerializer(home_players_data, many=True).data
            away_team_serialized = MatchDataSerializer(away_players_data, many=True).data

            return Response({
                'home_team': home_team_serialized,
                'away_team': away_team_serialized
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)