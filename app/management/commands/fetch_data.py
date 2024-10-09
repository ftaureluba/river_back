from django.core.management.base import BaseCommand

from app.services import getMatchSofascore

class Command(BaseCommand):
    help = 'Fetch and store data from an external API'

    def handle(self, *args, **kwargs):
        datos = getMatchSofascore.data_sofascore()
