from django.core.management.base import BaseCommand
from app.utils import fetch_and_store_data

class Command(BaseCommand):
    help = 'Fetch and store data from an external API'

    def handle(self, *args, **kwargs):
        api_url = 'https://v3.football.api-sports.io/players?season=2024&team=435' #aca al fondo hay q agregar &page=2 hasta la pagination (Buscar como automatizar)  
        fetch_and_store_data(api_url)
        self.stdout.write(self.style.SUCCESS('Successfully fetched and stored data'))
