import time
from bs4 import BeautifulSoup
import requests
from app.models import JugadorModel,Possession, ShootingModel, GoalAndShotCreation, GoalkeeperStats, Passing, PassTypes, DefensiveActions
from django.db import transaction
from app.services.requestDataFBREF import data

def request():
    url = "https://fbref.com/en/comps/21/Liga-Profesional-Argentina-Stats"

    res = requests.get(url)

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        try:
            tabla_general = soup.find('table', {'id':'stats_squads_standard_for'})

            equipo = tabla_general.find_all('tr')

            for row in equipo:
                datos = row.find_all('a')
                for x in datos:
                    original_href = x.get('href')  # Get the original href
                    text = x.text.strip()  # Extract the team's name
                    
                    # Construct the new URL
                    if original_href:
                        base_url = "https://fbref.com"
                        # Extract team ID from the original href
                        split_href = original_href.split('/')
                        team_id = split_href[3]  # 'ef99c78c' in your example
                        
                        # Build the proper URL
                        formatted_url = f"{base_url}/en/squads/{team_id}/2024/all_comps/{split_href[-1]}-All-Competitions"
                        
                        # Call the `data` function with the new URL
                        data(formatted_url, text)
                        print(f"URL: {formatted_url}, Content: {text}, importado con exito(?")
                        
                        # Delay to avoid being flagged
                        time.sleep(10)
        except:

            print('no encontre la tabla')