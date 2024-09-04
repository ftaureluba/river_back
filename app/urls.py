from django.urls import path
from . import views
from .views import JugadorListCreate

urlpatterns = [
    path("", views.home, name="home"),
    path("/api/jugadores/", JugadorListCreate.as_view(), name = 'jugador-list-create')
]
