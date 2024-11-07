from django.urls import path
from . import views
from .views import JugadorListCreate, MatchStatsAPIView

urlpatterns = [
    path('api/jugadores/', JugadorListCreate.as_view(), name = 'jugador-list-create'),
    path('api/match-stats/', MatchStatsAPIView.as_view(), name='match-stats-list-create')
]
