from bs4 import BeautifulSoup
import requests
from app.models import JugadorModel, ShootingModel, GoalAndShotCreation, GoalkeeperStats, Passing, PassTypes, DefensiveActions
from django.db import transaction

#, 'id': 'stats_shooting_combined'
def data():

    url = 'https://fbref.com/en/squads/ef99c78c/2024/all_comps/River-Plate-Stats-All-Competitions'
    res = requests.get(url)

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        
        general_table = soup.find('table',{'id': 'stats_standard_combined'})
        goalkeeping_table = soup.find('table', {'id':'stats_keeper_adv_combined'}) 
        shooting_table = soup.find('table', {'id' : 'stats_shooting_combined'})
        passing_table = soup.find('table', {'id' : 'stats_passing_combined'})
        pass_types = soup.find('table', {'id' : 'stats_passing_types_combined'})
        goal_and_shot_creation_table = soup.find('table', {'id' : 'stats_gca_combined'})
        defensive_table = soup.find('table', {'id' : 'stats_defense_combined'})

        datos_posta = []
        if general_table:
            coso = general_table.find_all('tr')
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
              
    if shooting_table:
            shooting_rows = shooting_table.find_all('tr')
            for row in shooting_rows[2:]:
                data = row.find_all(['th', 'td']) 
                shooting_data = [celda.get_text(strip=True) for celda in data]
                
                player_name = shooting_data[0]
                goals = int(shooting_data[5]) if shooting_data[5] else 0
                shots_total = int(shooting_data[6]) if shooting_data[6] else 0
                shots_on_target = int(shooting_data[7]) if shooting_data[7] else 0
                shot_accuracy = float(shooting_data[8]) if shooting_data[8] else 0.0
                shots_per_ninety = float(shooting_data[9]) if shooting_data[9] else 0.0
                shots_on_target_per_ninety = float(shooting_data[10]) if shooting_data[10] else 0.0
                goals_per_shot = float(shooting_data[11]) if shooting_data[11] else 0.0
                goals_per_shot_on_target = float(shooting_data[12]) if shooting_data[12] else 0.0
                average_shot_distance = float(shooting_data[13]) if shooting_data[13] else 0.0
                shots_from_freekick = int(shooting_data[14]) if shooting_data[14] else 0
                penalty_kicks_made = int(shooting_data[15]) if shooting_data[15] else 0
                penalty_kicks_attempted = int(shooting_data[16]) if shooting_data[16] else 0
                expected_goals = float(shooting_data[17]) if shooting_data[17] else 0.0
                non_penalty_expected_goals = float(shooting_data[18]) if shooting_data[18] else 0.0
                non_penalty_expected_goals_per_shot = float(shooting_data[19]) if shooting_data[19] else 0.0
                goals_minus_expected_goals = float(shooting_data[20]) if shooting_data[20] else 0.0
                non_penalty_goals_minus_non_penalty_expected_goals = float(shooting_data[21]) if shooting_data[21] else 0.0

                player = JugadorModel.objects.filter(player=player_name).first()
                with transaction.atomic():
                    if player:
                        ShootingModel.objects.update_or_create(
                            player=player,
                            defaults={
                                'shotsTotal': shots_total,
                                'shotsOnTarget': shots_on_target,
                                'goals': goals,
                                'percentShotsOnTarget': shot_accuracy,
                                'shotsPerNinety': shots_per_ninety,
                                'shotsOnTargetPerNinety': shots_on_target_per_ninety,
                                'goalsPerShot': goals_per_shot,
                                'goalsPerShotOnTarget': goals_per_shot_on_target,
                                'averageShotDistance': average_shot_distance,
                                'shotFromFreekicks': shots_from_freekick,
                                'penaltyKicks': penalty_kicks_made,
                                'penaltyKicksAttempted': penalty_kicks_attempted,
                                'expectedGoals': expected_goals,
                                'nonPenaltyExpectedGoals': non_penalty_expected_goals,
                                'nonPenaltyExpectedGoalsPerShot': non_penalty_expected_goals_per_shot,
                                'goalsMinusExpectedGoals': goals_minus_expected_goals,
                                'nonPenaltyGoalsMinusNonPenaltyExpectedGoals': non_penalty_goals_minus_non_penalty_expected_goals
                            }
                        )
                
    if goalkeeping_table:
            goalkeeping_rows = goalkeeping_table.find_all('tr')
            for row in goalkeeping_rows[2:]:
                data = row.find_all(['th', 'td']) 
                goalkeeping_data = [celda.get_text(strip=True) for celda in data]
                
                player_name = goalkeeping_data[0]
                goals_against = int(goalkeeping_data[5]) if goalkeeping_data[5] else 0
                penalty_kicks_allowed = int(goalkeeping_data[6]) if goalkeeping_data[6] else 0
                free_kicks = int(goalkeeping_data[7]) if goalkeeping_data[7] else 0
                corner_kicks = int(goalkeeping_data[8]) if goalkeeping_data[8] else 0
                own_goals = int(goalkeeping_data[9]) if goalkeeping_data[9] else 0

                
                psxg = float(goalkeeping_data[10]) if goalkeeping_data[10] else 0.0
                psxg_sot = float(goalkeeping_data[11]) if goalkeeping_data[11] else 0.0
                psxg_plus_minus = float(goalkeeping_data[12]) if goalkeeping_data[12] else 0.0
                psxg_per_90 = float(goalkeeping_data[13]) if goalkeeping_data[13] else 0.0

                
                launched_cmp = int(goalkeeping_data[14]) if goalkeeping_data[14] else 0
                launched_att = int(goalkeeping_data[15]) if goalkeeping_data[15] else 0
                launched_cmp_pct = float(goalkeeping_data[16]) if goalkeeping_data[16] else 0.0

                
                passes_att = int(goalkeeping_data[17]) if goalkeeping_data[17] else 0
                passes_thrown = int(goalkeeping_data[18]) if goalkeeping_data[18] else 0
                passes_launch_pct = float(goalkeeping_data[19]) if goalkeeping_data[19] else 0.0
                passes_avg_length = float(goalkeeping_data[20]) if goalkeeping_data[20] else 0.0

                
                goal_kicks_att = int(goalkeeping_data[21]) if goalkeeping_data[21] else 0
                goal_kicks_launch_pct = float(goalkeeping_data[22]) if goalkeeping_data[22] else 0.0
                goal_kicks_avg_length = float(goalkeeping_data[23]) if goalkeeping_data[23] else 0.0

                
                crosses_opp = int(goalkeeping_data[24]) if goalkeeping_data[24] else 0
                crosses_stopped = int(goalkeeping_data[25]) if goalkeeping_data[25] else 0
                crosses_stopped_pct = float(goalkeeping_data[26]) if goalkeeping_data[26] else 0.0

                
                sweeper_opa = int(goalkeeping_data[27]) if goalkeeping_data[27] else 0
                sweeper_opa_per_90 = float(goalkeeping_data[28]) if goalkeeping_data[28] else 0.0
                sweeper_avg_dist = float(goalkeeping_data[29]) if goalkeeping_data[29] else 0.0

                player = JugadorModel.objects.filter(player=player_name).first()

                with transaction.atomic():
                    if player:
                        GoalkeeperStats.objects.update_or_create(
                            player=player,
                            defaults={
                                
                                'goalsAgainst': goals_against,
                                'penaltiesAgainst': penalty_kicks_allowed,
                                'freeKicksAgainst': free_kicks,
                                'cornerKicksAgainst': corner_kicks,
                                'ownGoals': own_goals,
                                'postShotExpectedGoals': psxg,
                                'psxgPerShotOnTarget': psxg_sot,
                                'psxgGoalDifference': psxg_plus_minus,
                                'psxgPer90': psxg_per_90,
                                'launchedCompleted': launched_cmp,
                                'launchedAttempted': launched_att,
                                'launchCompletionPercentage': launched_cmp_pct,
                                'goalkeeperPassesAttempted': passes_att,
                                'throwsAttempted': passes_thrown,
                                'launchPassesPercentage': passes_launch_pct,
                                'launchAvgLength': passes_avg_length,
                                'goalKicksAttemptedOther': goal_kicks_att,
                                'goalKicksLaunchPercentage': goal_kicks_launch_pct,
                                'goalKicksAvgLength': goal_kicks_avg_length,
                                'crossesFaced': crosses_opp,
                                'crossesStopped': crosses_stopped,
                                'crossesStoppedPercentage': crosses_stopped_pct,
                                'sweeperActions': sweeper_opa,
                                'sweeperActionsPer90': sweeper_opa_per_90,
                                'avgDistanceOfSweeperActions': sweeper_avg_dist
                            }
                        )
        
    else: 
        print(f'error en el request {res.status_code}')
    return dict_datos


