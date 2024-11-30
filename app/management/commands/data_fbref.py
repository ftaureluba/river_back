from django.core.management.base import BaseCommand
from app.services.requestData import request

class Command(BaseCommand):
    help = 'Fetch and store data from an external API'

    def handle(self, *args, **kwargs):
        
        datos = request()
        
        self.stdout.write(self.style.SUCCESS('Ahi importe la data infeliz'))

        #actualizar_db(datos)
        self.stdout.write(self.style.SUCCESS('bien ahi perri actualice la db.'))