import time
from bs4 import BeautifulSoup
import requests
from app.models import JugadorModel,Possession, ShootingModel, GoalAndShotCreation, GoalkeeperStats, Passing, PassTypes, DefensiveActions
from django.db import transaction

def data(url, team):

    time.sleep(10)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    res = requests.get(url, headers=header, timeout=10) #aca puedo pasar el equipo(como slug o como convenga) para guardarlo en un campo
    try:
        if res.status_code == 200:
            print('entre????')
            soup = BeautifulSoup(res.text, 'html.parser')
            
            general_table = soup.find('table',{'id': 'stats_standard_combined'})
            goalkeeping_table = soup.find('table', {'id':'stats_keeper_adv_combined'}) 
            shooting_table = soup.find('table', {'id' : 'stats_shooting_combined'})
            passing_table = soup.find('table', {'id' : 'stats_passing_combined'})
            pass_types = soup.find('table', {'id' : 'stats_passing_types_combined'})
            goal_and_shot_creation_table = soup.find('table', {'id' : 'stats_gca_combined'})
            defensive_table = soup.find('table', {'id' : 'stats_defense_combined'})
            possession_table = soup.find('table', {'id': 'stats_possession_combined'})

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
                #imaginando que aca tengo lo del equipo implementado:
                equipo = team 
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
                            'team' : equipo
                        }
                    )
            print('pase el primer coso')       
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
            print('pase shooting table')
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
            print('pase goalkeeping table')
            if passing_table:
                passing_rows = passing_table.find_all('tr')
                for row in passing_rows[2:]:  # Skip the header rows
                    data = row.find_all(['th', 'td']) 
                    passing_data = [celda.get_text(strip=True) for celda in data]

                    player_name = passing_data[0]
                    
                    
                    completed = int(passing_data[5]) if passing_data[5] else 0
                    attempted = int(passing_data[6]) if passing_data[6] else 0
                    completed_percentage = float(passing_data[7]) if passing_data[7] else 0.0
                    total_distance = int(passing_data[8]) if passing_data[8] else 0
                    progressive_distance = int(passing_data[9]) if passing_data[9] else 0

                    short_completed = int(passing_data[10]) if passing_data[10] else 0
                    short_attempted = int(passing_data[11]) if passing_data[11] else 0
                    short_completed_percentage = float(passing_data[12]) if passing_data[12] else 0.0

                    medium_completed = int(passing_data[13]) if passing_data[13] else 0
                    medium_attempted = int(passing_data[14]) if passing_data[14] else 0
                    medium_completed_percentage = float(passing_data[15]) if passing_data[15] else 0.0

                    long_completed = int(passing_data[16]) if passing_data[16] else 0
                    long_attempted = int(passing_data[17]) if passing_data[17] else 0
                    long_completed_percentage = float(passing_data[18]) if passing_data[18] else 0.0

                    assists = int(passing_data[19]) if passing_data[19] else 0
                    expected_assisted_goals = float(passing_data[20]) if passing_data[20] else 0.0
                    expected_assists = float(passing_data[21]) if passing_data[21] else 0.0
                    assists_minus_expected_goals_assisted = float(passing_data[22]) if passing_data[22] else 0.0
                    key_passes = int(passing_data[23]) if passing_data[23] else 0
                    passes_into_final_third = int(passing_data[24]) if passing_data[24] else 0
                    passes_into_penalty_area = int(passing_data[25]) if passing_data[25] else 0
                    crosses_into_penalty_area = int(passing_data[26]) if passing_data[26] else 0
                    progressive_passes = int(passing_data[27]) if passing_data[27] else 0

                    player = JugadorModel.objects.filter(player=player_name).first()

                    with transaction.atomic():
                        if player:
                            Passing.objects.update_or_create(
                                player=player,
                                defaults={
                                    'completed': completed,
                                    'attempted': attempted,
                                    'completedPercentage': completed_percentage,
                                    'totalDistance': total_distance,
                                    'totalProgressiveDistance': progressive_distance,
                                    'shortCompleted': short_completed,
                                    'shortAttempted': short_attempted,
                                    'shortCompletedPercentage': short_completed_percentage,
                                    'mediumCompleted': medium_completed,
                                    'mediumAttempted': medium_attempted,
                                    'mediumCompletedPercentage': medium_completed_percentage,
                                    'longCompleted': long_completed,
                                    'longAttempted': long_attempted,
                                    'longCompletedPercentage': long_completed_percentage,
                                    'assists': assists,
                                    'expectedAssistedGoals': expected_assisted_goals,
                                    'expectedAssists': expected_assists,
                                    'assistsMinusExpectedGoalsAssisted': assists_minus_expected_goals_assisted,
                                    'keyPasses': key_passes,
                                    'passesIntoTheFinalThird': passes_into_final_third,
                                    'passesIntoPenaltyArea': passes_into_penalty_area,
                                    'crossesIntoPenaltyArea': crosses_into_penalty_area,
                                    'progressivePasses': progressive_passes
                                }
                            )
            print('pase passing table')
            if pass_types:
                pass_types_rows = pass_types.find_all('tr')
                for row in pass_types_rows[2:]:
                    data = row.find_all(['th', 'td'])
                    pass_types_data = [celda.get_text(strip=True) for celda in data]
                    
                    player_name = pass_types_data[0]

                    passesAttempted = int(pass_types_data[5]) if pass_types_data[5] else 0
                    livePasses = int(pass_types_data[6]) if pass_types_data[6] else 0
                    deadPasses = int(pass_types_data[7]) if pass_types_data[7] else 0
                    freeKicks = int(pass_types_data[8]) if pass_types_data[8] else 0
                    throughBalls = int(pass_types_data[9]) if pass_types_data[9] else 0
                    switches = int(pass_types_data[10]) if pass_types_data[10] else 0
                    crosses = int(pass_types_data[11]) if pass_types_data[11] else 0
                    throwIns = int(pass_types_data[12]) if pass_types_data[12] else 0
                    corners = int(pass_types_data[13]) if pass_types_data[13] else 0
                    cornersIn = int(pass_types_data[14]) if pass_types_data[14] else 0
                    cornersOut = int(pass_types_data[15]) if pass_types_data[15] else 0
                    cornersStraight = int(pass_types_data[16]) if pass_types_data[16] else 0
                    passesCompleted = int(pass_types_data[17]) if pass_types_data[17] else 0
                    passesOffside = int(pass_types_data[18]) if pass_types_data[18] else 0
                    passesBlocked = int(pass_types_data[19]) if pass_types_data[19] else 0
                    
                    player = JugadorModel.objects.filter(player=player_name).first()

                    with transaction.atomic():
                        if player: 
                            PassTypes.objects.update_or_create(
                                player = player,
                                defaults={
                                    'passesAttempted':passesAttempted,
                                    'livePasses':livePasses,
                                    'deadPasses': deadPasses,
                                    'freeKicks': freeKicks,
                                    'throughBalls': throughBalls,
                                    'switches': switches,
                                    'crosses': crosses,
                                    'throwIns': throwIns,
                                    'corners': corners,
                                    'cornersIn': cornersIn,
                                    'cornersOut': cornersOut,
                                    'cornersStraight': cornersStraight,
                                    'passesCompleted': passesCompleted,
                                    'passesOffside': passesOffside,
                                    'passesBlocked': passesBlocked
                                }
                            )
            print('pase pass types')
            if goal_and_shot_creation_table:
                gc_rows = goal_and_shot_creation_table.find_all('tr')
                for row in gc_rows[2:]:
                    data = row.find_all(['th', 'td'])
                    gc_data = [celda.get_text(strip=True) for celda in data]
                    
                    player_name = gc_data[0]

                    shotCreatiingAction = int(gc_data[5]) if gc_data[5] else 0
                    shotCreatiingActionPerNinety = float(gc_data[6]) if gc_data[6] else 0.0
                    liveSCA = int(gc_data[7]) if gc_data[7] else 0
                    deadSCA = int(gc_data[8]) if gc_data[8] else 0
                    takeOnSCA = int(gc_data[9]) if gc_data[9] else 0
                    shotSCA = int(gc_data[10]) if gc_data[10] else 0
                    fouldDrawnSCA = int(gc_data[11]) if gc_data[11] else 0
                    defensiveSCA = int(gc_data[12]) if gc_data[12] else 0
                    goalCreatingAction = int(gc_data[13]) if gc_data[13] else 0
                    goalCreatingActionPerNinety = float(gc_data[14]) if gc_data[14] else 0.0
                    liveGCA = int(gc_data[15]) if gc_data[15] else 0
                    deadGCA = int(gc_data[16]) if gc_data[16] else 0
                    takeOnGCA = int(gc_data[17]) if gc_data[17] else 0
                    shotGCA = int(gc_data[18]) if gc_data[18] else 0
                    fouldDrawnGCA = int(gc_data[19]) if gc_data[19] else 0
                    defensiveGCA = int(gc_data[20]) if gc_data[20] else 0


                    player = JugadorModel.objects.filter(player=player_name).first()

                    with transaction.atomic():
                        if player: 
                            GoalAndShotCreation.objects.update_or_create(
                                player = player,
                                defaults={
                                    'shotCreatiingAction':shotCreatiingAction,
                                    'shotCreatiingActionPerNinety':shotCreatiingActionPerNinety,
                                    'liveSCA': liveSCA,
                                    'deadSCA': deadSCA,
                                    'takeOnSCA': takeOnSCA,
                                    'shotSCA': shotSCA,
                                    'fouldDrawnSCA': fouldDrawnSCA,
                                    'defensiveSCA': defensiveSCA,
                                    'goalCreatingAction': goalCreatingAction,
                                    'goalCreatingActionPerNinety': goalCreatingActionPerNinety,
                                    'liveGCA': liveGCA,
                                    'deadGCA': deadGCA,
                                    'takeOnGCA': takeOnGCA,
                                    'shotGCA': shotGCA,
                                    'fouldDrawnGCA': fouldDrawnGCA,
                                    'defensiveGCA': defensiveGCA
                                }
                            )
            print('pase goal and shot creation')
            if defensive_table:
                    defensive_rows = defensive_table.find_all('tr')
                    for row in defensive_rows[2:]:
                        data = row.find_all(['th', 'td'])
                        defensive_data = [celda.get_text(strip=True) for celda in data]
                        
                        player_name = defensive_data[0]

                        tackles = int(defensive_data[5]) if defensive_data[5] else 0
                        tacklesWon = int(defensive_data[6]) if defensive_data[6] else 0
                        tacklesDefensiveThird = int(defensive_data[7]) if defensive_data[7] else 0
                        tacklesMiddleThird = int(defensive_data[8]) if defensive_data[8] else 0
                        tacklesAttackingThird = int(defensive_data[9]) if defensive_data[9] else 0
                        dribblersTackled = int(defensive_data[10]) if defensive_data[10] else 0
                        dribblesChallenged = int(defensive_data[11]) if defensive_data[11] else 0
                        dribblersTackledPercentage = float(defensive_data[12]) if defensive_data[12] else 0.0
                        challengesLost = int(defensive_data[13]) if defensive_data[13] else 0
                        blocks = int(defensive_data[14]) if defensive_data[14] else 0
                        shotsBlocked = int(defensive_data[15]) if defensive_data[15] else 0
                        passesBlocked = int(defensive_data[16]) if defensive_data[16] else 0
                        interceptions = int(defensive_data[17]) if defensive_data[17] else 0
                        tacklesPlusInterceptions = int(defensive_data[18]) if defensive_data[18] else 0
                        clearances = int(defensive_data[19]) if defensive_data[19] else 0
                        errors = int(defensive_data[20]) if defensive_data[20] else 0


                        player = JugadorModel.objects.filter(player=player_name).first()

                        with transaction.atomic():
                            if player: 
                                DefensiveActions.objects.update_or_create(
                                    player = player,
                                    defaults={
                                        'tackles':tackles,
                                        'tacklesWon':tacklesWon,
                                        'tacklesDefensiveThird': tacklesDefensiveThird,
                                        'tacklesMiddleThird': tacklesMiddleThird,
                                        'tacklesAttackingThird': tacklesAttackingThird,
                                        'dribblersTackled': dribblersTackled,
                                        'dribblesChallenged': dribblesChallenged,
                                        'dribblersTackledPercentage': dribblersTackledPercentage,
                                        'challengesLost': challengesLost,
                                        'blocks': blocks,
                                        'shotsBlocked': shotsBlocked,
                                        'passesBlocked': passesBlocked,
                                        'interceptions': interceptions,
                                        'tacklesPlusInterceptions': tacklesPlusInterceptions,
                                        'clearances': clearances,
                                        'errors': errors
                                    }
                                )            
            print('pase defensive table')
            if possession_table:
                possession_rows = possession_table.find_all('tr')
                for row in possession_rows[2:]:
                    data = row.find_all(['th', 'td'])
                    possession_data = [celda.get_text(strip=True) for celda in data]

                    player_name = possession_data[0]

                    touches = int(possession_data[5]) if possession_data[5] else 0
                    touchesPenaltyArea = int(possession_data[6]) if possession_data[6] else 0
                    touchesDefense = int(possession_data[7]) if possession_data[7] else 0
                    touchesMiddle = int(possession_data[8]) if possession_data[8] else 0
                    touchesOffense = int(possession_data[9]) if possession_data[9] else 0
                    touchesOpponentPenaltyArea = int(possession_data[10]) if possession_data[10] else 0
                    touchesLiveBall = int(possession_data[11]) if possession_data[11] else 0
                    takeOnAttempted = int(possession_data[12]) if possession_data[12] else 0
                    takeOnSuccesful = int(possession_data[13]) if possession_data[13] else 0
                    takeOnSuccesfulPorcentage = float(possession_data[14]) if possession_data[14] else 0.0
                    takeOnTackled = int(possession_data[15]) if possession_data[15] else 0
                    takeOnTackledPorcentage = float(possession_data[16]) if possession_data[16] else 0.0
                    carries  = int(possession_data[17]) if possession_data[17] else 0
                    carriesTotalDistance = int(possession_data[18]) if possession_data[18] else 0
                    carriesProgressiveDistance = int(possession_data[19]) if possession_data[19] else 0
                    progressiveCarries = int(possession_data[20]) if possession_data[20] else 0
                    carriesIntoFinalThird = int(possession_data[21]) if possession_data[21] else 0
                    carriesIntoPenaltyArea = int(possession_data[22]) if possession_data[22] else 0
                    miscontrols = int(possession_data[23]) if possession_data[23] else 0
                    dispossessed = int(possession_data[24]) if possession_data[24] else 0
                    passesReceived = int(possession_data[25]) if possession_data[25] else 0
                    passesReceivedProgressive = int(possession_data[26]) if possession_data[26] else 0

                    player = JugadorModel.objects.filter(player=player_name).first()

                    with transaction.atomic():
                        if player:
                            Possession.objects.update_or_create(
                                player = player,
                                defaults={
                                    
                                    'touches':touches,
                                    'touchesPenaltyArea':touchesPenaltyArea,
                                    'touchesDefense': touchesDefense,
                                    'touchesMiddle':touchesMiddle,
                                    'touchesOffense':touchesMiddle,
                                    'touchesOpponentPenaltyArea':touchesOpponentPenaltyArea,
                                    'touchesLiveBall':touchesLiveBall,
                                    'takeOnAttempted':takeOnAttempted,
                                    'takeOnSuccesful':takeOnSuccesful,
                                    'takeOnSuccesfulPorcentage':takeOnSuccesfulPorcentage,
                                    'takeOnTackled':takeOnTackled,
                                    'takeOnTackledPorcentage':takeOnTackledPorcentage,
                                    'carries':carries,
                                    'carriesTotalDistance':carriesTotalDistance,
                                    'carriesProgressiveDistance':carriesProgressiveDistance,
                                    'progressiveCarries':progressiveCarries,
                                    'carriesIntoFinalThird':carriesIntoFinalThird,
                                    'carriesIntoPenaltyArea':carriesIntoPenaltyArea,
                                    'miscontrols':miscontrols,
                                    'dispossessed':dispossessed,
                                    'passesReceived':passesReceived,
                                    'passesReceivedProgressive':passesReceivedProgressive
                                }
                            )
            print('pase possesion table')
        else: 
            print(f'error en el request {res.status_code}')
    except requests.exceptions.Timeout:
        print('timeout....')
        time.sleep(30)
        data(url,team)
    except Exception as e:
        print('error ocurred:', e)
    return dict_datos


