from django.db import transaction
import requests
from .models import TeamModel, LeagueModel, StatisticsModel, PlayerModel

def fetch_and_store_data(api_url):
    payload = {}
    headers = {
        'x-apisports-key': '458eeb450f943c842e3a2b52df93a558',
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        players_data = response.json().get('response', [])

        
        with transaction.atomic():
            for player_data in players_data:
                player_info = player_data['player']
                
                
                player, created = PlayerModel.objects.update_or_create(
                    id=player_info['id'],
                    defaults={
                        'name': player_info.get('name', ''),
                        'firstname': player_info.get('firstname', ''),
                        'lastname': player_info.get('lastname', ''),
                        'age': player_info.get('age', None),
                        'birth_info': player_info.get('birth', {}),
                        'nationality': player_info.get('nationality', ''),
                        'height': player_info.get('height', ''),
                        'weight': player_info.get('weight', ''),
                        'injured': player_info.get('injured', False),
                        'photo': player_info.get('photo', ''),
                    }
                )

                for estadistica in player_data['statistics']:
                    
                    team, created = TeamModel.objects.update_or_create(
                        id=estadistica['team']['id'],
                        defaults={
                            'name': estadistica['team']['name'],
                            'logo': estadistica['team']['logo']
                        }
                    )

                    
                    league, created = LeagueModel.objects.update_or_create(
                        id=estadistica['league']['id'],
                        defaults={
                            'name': estadistica['league']['name'],
                            'country': estadistica['league'].get('country', ''),
                            'logo': estadistica['league'].get('logo', ''),
                            'flag': estadistica['league'].get('flag', ''),
                            'season': estadistica['league']['season'],
                        }
                    )

                    
                    stats = {
                        'games': estadistica.get('games', {}),
                        'substitutes': estadistica.get('substitutes', {}),
                        'shots': estadistica.get('shots', {}),
                        'goals': estadistica.get('goals', {}),
                        'passes': estadistica.get('passes', {}),
                        'tackles': estadistica.get('tackles', {}),
                        'duels': estadistica.get('duels', {}),
                        'dribbles': estadistica.get('dribbles', {}),
                        'fouls': estadistica.get('fouls', {}),
                        'cards': estadistica.get('cards', {}),
                        'penalty': estadistica.get('penalty', {})
                    }

                    
                    statistics = StatisticsModel.objects.create(
                        team=team,
                        league=league,
                        statistics=stats
                    )

                    # aca hago un 'puntero' a statistics
                    player.stats.add(statistics)
                    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
