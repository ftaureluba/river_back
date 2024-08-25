from django.core.management.base import BaseCommand
from app.utils import print_goleadores

class Command(BaseCommand):
    help = 'Fetch and store data from an external API'

    def handle(self, *args, **kwargs):
        
        print_goleadores()
        self.stdout.write(self.style.SUCCESS('Aca estan los goleadores chupapija'))