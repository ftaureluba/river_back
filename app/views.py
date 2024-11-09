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
            match_data = MatchData.objects.all()
            
            serialized_data = MatchDataSerializer(match_data, many=True).data

            return Response({
                'home_team': serialized_data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
