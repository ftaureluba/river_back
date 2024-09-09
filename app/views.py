from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import *
from rest_framework import generics
import requests
from .serializers import JugadorSerializer




class JugadorListCreate(generics.ListCreateAPIView):
    queryset = JugadorModel.objects.select_related(
    'shootingmodel', 
    'goalandshotcreation', 
    'goalkeeperstats', 
    'defensiveactions', 
    'passing', 
    'passtypes'
    ).all()
    serializer_class = JugadorSerializer
