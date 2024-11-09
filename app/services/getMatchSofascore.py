from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import pandas as pd
import http.client
from app.models import MatchData
import requests
from django.db import transaction

pd.set_option('display.max_columns', None)  
pd.set_option('display.max_rows', None)     

class InvalidStrType(Exception):
    def __init__(self, param):
        self.message = f"{param} must be a string.\n{param} debe ser un string"
        super().__init__(self.message)


class MatchDoesntHaveInfo(Exception):
    def __init__(self, path):
        self.message = f"Match in path {path} doesn't have enough information for this functions, try with another one.\nEl partido en el path {path} no tiene la información para estas funciones, pruebe con otro."
        super().__init__(self.message)


class SofaScoreScraper:
    # Method to get match ID
    def get_match_id(self, match_url):
        if type(match_url) != str:
            raise InvalidStrType(match_url)
        match_id = match_url.split(':')[-1]
        return match_id

    def get_team_names(self, match_url):
        """Get the team names for the home and away teams

        Args:
            match_url (string): Full link to a SofaScore match

        Returns:
            strings: Name of home and away team.
        """

        data = self.get_match_data(match_url)

        try:
            home_team = data['event']['homeTeam']['name']
        except KeyError:
            raise MatchDoesntHaveInfo(match_url)
        
        away_team = data['event']['awayTeam']['name']

        return home_team, away_team

    def get_match_data(self, match_url):
        """Gets all the general data from a match 

        Args:
            match_url (str): Full link to a SofaScore match

        Returns:
            json: Data of the match.
        """
        
        match_id = self.get_match_id(match_url)
        
        url = f'api/v1/event/{match_id}'
        
        data = self.httpclient_request(url)
        
        time.sleep(3)
        
        json_data = json.loads(data)
        
        return json_data

    def get_players_match_stats(self, match_url):
        match_id = self.get_match_id(match_url)
        home_name, away_name = self.get_team_names(match_url)
        
        request_url = f'api/v1/event/{match_id}/lineups'
        
        data = self.httpclient_request(request_url)  
        response = json.loads(data)
        target_team = "River Plate"
        if home_name == target_team:
            team_key = 'home'
            team_name = home_name
        elif away_name == target_team:
            team_key = 'away'
            team_name = away_name

        data = pd.DataFrame(response[team_key]['players'])
    
        
        try:
            columns_list = [
                data['player'].apply(lambda x : x.get('name') if isinstance(x, dict) else None),
                data['shirtNumber'], 
                data['position'], 
                data['substitute'],
                data['statistics'].apply(lambda x: x.get('minutesPlayed') if isinstance(x, dict) else None).fillna(0),  # Replace NaN with None
                data['statistics'].apply(lambda x: x.get('rating') if isinstance(x, dict) else None).fillna(0),
                data['captain'].fillna(False)
            ]
        except KeyError:
            raise MatchDoesntHaveInfo(match_url)
        
        df = pd.concat(columns_list, axis=1)
        df.columns = [
        'player', 'shirtNumber', 'position', 'substitute', 
        'minutesPlayed', 'rating', 'captain'
        ]
        df['team'] = team_name
        
        return df 


    def httpclient_request(self, path):
        """Request used to SofaScore

        Args:
            path (str): Part of the url to make the request

        Returns:
            data: _description_
        """
        time.sleep(5)
        url = "api.sofascore.com"

        conn = http.client.HTTPSConnection(url)

        conn.request("GET", path)

        res = conn.getresponse()

        data = res.read()

        conn.close()
        
        return data
    
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.set_window_size(1920, 1080)  
    return driver

def data_sofascore():
    driver = init_driver()
    
    try:
        RIVER_URL = 'https://www.sofascore.com/team/football/river-plate/3211'
        print(f"Fetching data from: {RIVER_URL}")
        driver.get(RIVER_URL)

        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        try:
            req = requests.get("https://www.sofascore.com/api/v1/team/3211/performance")
            recent_form = req.json()
            ultimo_partido = recent_form['events'][-1]
            custom_id = ultimo_partido['customId']
            id = ultimo_partido['id']
            slug = ultimo_partido['slug']
        finally:

        
            last_match_url = f"https://sofascore.com/football/match/{slug}/{custom_id}#id:{id}"
            scraper = SofaScoreScraper()
            df = scraper.get_players_match_stats(last_match_url)
            
            match_data_list = [
                MatchData(
                    player_name=row['player'],
                    jersey_number=row['shirtNumber'],
                    position=row['position'],
                    is_substitute=row['substitute'],
                    minutes_played=row['minutesPlayed'],
                    rating=row['rating'],
                    is_captain=row['captain'],
                    team='home',
                    player_id=row.get('id')
                )
                for _, row in df.iterrows()
            ]

            with transaction.atomic():
                MatchData.objects.all().delete()
                MatchData.objects.bulk_create(match_data_list)
            
            print(df)
            print("Data saved to the database successfully.")
            
    
    finally:
        driver.quit()
    return df



