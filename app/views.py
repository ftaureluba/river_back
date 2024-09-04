from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import *
from rest_framework import generics
import requests
from .serializers import JugadorSerializer


'''
def generate_request(url, params={}):
    payload={}
    headers = {
        'x-apisports-key': '458eeb450f943c842e3a2b52df93a558',
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        return response.json()
    else: 
        return {}


def home(request):
    data = generate_request("https://v3.football.api-sports.io/players?season=2024&team=435")
    response_data = []

    for jugador in data['response']:
        player_data = PlayerSerializer(jugador['player']).data
        statistics_data = StatisticsSerializer(jugador['statistics'], many=True).data
        player_data['statistics'] = statistics_data
        response_data.append(
            player_data
        )

    return JsonResponse(response_data, safe=False)
    return HttpResponse('vamosriverlareputaquetepario')
'''

class JugadorListCreate(generics.ListCreateAPIView):
    queryset = JugadorModel.objects.all()
    serializerClass = JugadorSerializer
