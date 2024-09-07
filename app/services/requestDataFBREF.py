from bs4 import BeautifulSoup
import requests
from app.models import JugadorModel
from django.db import transaction

#, 'id': 'stats_shooting_combined'
def data():

    url = 'https://fbref.com/en/squads/ef99c78c/2024/all_comps/River-Plate-Stats-All-Competitions'
    res = requests.get(url)

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        
        tablas = soup.find('table',{'id': 'stats_standard_combined'}) 
        datos_posta = []
        if tablas:
            coso = tablas.find_all('tr')
            for row in coso:
                data = row.find_all(['th', 'td']) 
                cell_data = [celda.get_text(strip=True) for celda in data]
                datos_posta.append(cell_data)
                
        
        dict_datos = []
        
        for i in range (2, len(datos_posta)):
            coso = {}
            for j in range(0, len(datos_posta[1]) - 1):
                if datos_posta[1][j] in coso:
                  aux = datos_posta[1][j]
                  coso[f'{aux} per 90'] = datos_posta[i][j]
                  
                else:
                  coso[datos_posta[1][j]] = datos_posta[i][j]
            
            
            player_name = coso.get('Player', '')
            nation = coso.get('Nation', '')
            position = coso.get('Pos', '')
            age = coso.get('Age', '') 
            matches_played = int(coso.get('MP', '0') or '0')
            starts = int(coso.get('Starts', '0') or '0')
            minutes_played = coso.get('Min', '0')
            if len(minutes_played) > 4:
                minutes_played = minutes_played.replace(',', '')
                minutes_played=int(minutes_played)
            else : 
                minutes_played = int(minutes_played or 0)

            nineties = float(coso.get('90s', '0') or '0')
            goals = int(coso.get('Gls', '0') or '0')
            assists = int(coso.get('Ast', '0') or '0')
            goals_plus_assists = int(coso.get('G+A', '0') or '0')
            goals_minus_penalties = int(coso.get('G-PK', '0') or '0')
            penalties = int(coso.get('PK', '0') or '0')
            penalties_attempted = int(coso.get('PKatt', '0') or '0')
            yellow_cards = int(coso.get('CrdY', '0') or '0')
            red_cards = int(coso.get('CrdR', '0') or '0')
            expected_goals = float(coso.get('xG', '0.0') or '0.0')
            non_penalty_expected_goals = float(coso.get('npxG', '0.0') or '0.0')
            expected_assists = float(coso.get('xAG', '0.0') or '0.0')
            non_penalty_goals_plus_expected_assists = float(coso.get('npxG+xAG', '0.0') or '0.0')
            progressive_carries = int(coso.get('PrgC', '0') or '0')
            progressive_passes = int(coso.get('PrgP', '0') or '0')
            progressive_passes_received = int(coso.get('PrgR', '0') or '0')
            goals_per_ninety = float(coso.get('Gls per 90', '0.0') or '0.0')
            assists_per_ninety = float(coso.get('Ast per 90', '0.0') or '0.0')
            goals_plus_assists_per_ninety = float(coso.get('G+A per 90', '0.0') or '0.0')
            goals_minus_penalties_per_ninety = float(coso.get('G-PK per 90', '0.0') or '0.0')
            goals_plus_assists_minus_penalties_per_ninety = float(coso.get('G+A-PK', '0.0') or '0.0')
            expected_goals_per_ninety = float(coso.get('xG per 90', '0.0') or '0.0')
            expected_assists_per_ninety = float(coso.get('xAG per 90', '0.0') or '0.0')
            expected_goals_plus_assists_per_ninety = float(coso.get('xG+xAG', '0.0') or '0.0')
            non_penalty_expected_goals_per_ninety = float(coso.get('npxG per 90', '0.0') or '0.0')
            non_penalty_goals_plus_expected_assists_per_ninety = float(coso.get('npxG+xAG per 90', '0.0') or '0.0')


            with transaction.atomic():
                player, created = JugadorModel.objects.update_or_create(
                    player=player_name,
                    defaults={
                        'nation': nation,
                        'position': position,
                        'age': age,
                        'matchesPlayed': matches_played,
                        'starts': starts,
                        'minutesPlayed': minutes_played,
                        'nineties': nineties,
                        'goals': goals,
                        'assists': assists,
                        'goalsPlusAssists': goals_plus_assists,
                        'goalsMinusPenalties': goals_minus_penalties,
                        'penalties': penalties,
                        'penaltiesAttempted': penalties_attempted,
                        'yellowCards': yellow_cards,
                        'redCards': red_cards,
                        'expectedGoals': expected_goals,
                        'nonPenaltyExpectedGoals': non_penalty_expected_goals,
                        'expectedAssists': expected_assists,
                        'nonPenaltyGoalsPlusExpectedAssists': non_penalty_goals_plus_expected_assists,
                        'progressiveCarries': progressive_carries,
                        'progressivePasses': progressive_passes,
                        'progressivePassesReceived': progressive_passes_received,
                        'goalsPerNinety': goals_per_ninety,
                        'assistsPerNinety': assists_per_ninety,
                        'goalsPlusAssistsPerNinety': goals_plus_assists_per_ninety,
                        'goalsMinusPenaltiesPerNinety': goals_minus_penalties_per_ninety,
                        'goalsPlusAssistsMinusPenaltiesPerNinety': goals_plus_assists_minus_penalties_per_ninety,
                        'expectedGoalsPerNinety': expected_goals_per_ninety,
                        'expectedAssistsPerNinety': expected_assists_per_ninety,
                        'expectedGoalsPlusAssistsPerNinety': expected_goals_plus_assists_per_ninety,
                        'nonPenaltyExpectedGoalsPerNinety': non_penalty_expected_goals_per_ninety,
                        'nonPenaltyGoalsPlusExpectedAssistsPerNinety': non_penalty_goals_plus_expected_assists_per_ninety,
                    }
                )
        

        
        
    else: 
        print(f'error en el request {res.status_code}')
    return dict_datos


