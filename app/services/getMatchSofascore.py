from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Selenium WebDriver
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Set the window size to simulate desktop view
    driver.set_window_size(1920, 1080)  # Set a standard desktop resolution
    return driver

# Scrape data from the River Plate page
def data_sofascore():
    driver = init_driver()
    
    try:
        # Load the River Plate page
        RIVER_URL = 'https://www.sofascore.com/team/football/river-plate/3211'
        print(f"Fetching data from: {RIVER_URL}")
        driver.get(RIVER_URL)

        # Give time for page to load
        time.sleep(5)

        # Get the page source and parse it with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Step 1: Find the last match link
        last_matches_div = soup.find_all("div", {"class": "sc-dce818dc-0 cjKrdG"})
        if last_matches_div:
            match_links = last_matches_div[0].find_all('a')  # Select the first container and get the links
            if match_links:
                last_match_url = match_links[-1]['href']
                full_url = f"https://www.sofascore.com{last_match_url}"
                print(f"Last match URL: {full_url}")
                
                # Step 2: Load the match details page
                driver.get(full_url)
                time.sleep(5)

                # Step 3: Try clicking the button to load player panel (Using CSS Selector)
                try:
                    WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.Box.bkrWzf.Tab.cbSGUp.secondary"))
                    ).click()
                    print("Clicked to load player panel.")
                except Exception as e:
                    print(f"Failed to click the button: {e}")
                    driver.save_screenshot('error_screenshot.png')  # Take screenshot for debugging
                    return
                
                # Step 4: Parse the match details page again
                match_soup = BeautifulSoup(driver.page_source, 'html.parser')
                
                # Step 5: Extract player data (replace 'Table fEUhaC' and 'TabPanel bpHovE' with the real classes if needed)
                table = match_soup.find('div', {'data-panelid': '2', 'class': 'TabPanel bpHovE'})
                if table:
                    players_table = table.find('table', {'class': 'Table fEUhaC'})
                    if players_table:
                        players_table_rows = players_table.find_all('tr')
                        data = []
                        for row in players_table_rows:
                            cols = row.find_all('td')
                            if len(cols) > 1:
                                player_name = cols[1].text.strip()
                                rating = cols[-1].text.strip()
                                data.append((player_name, rating))
                        
                        # Print player data
                        for player, rating in data:
                            print(f"Player: {player}, Rating: {rating}")
                    else:
                        print("Players table not found.")
                else:
                    print("Player panel not found.")
            else:
                print("No match links found.")
        else:
            print("Match container not found.")
    
    finally:
        # Close the browser after scraping is done
        driver.quit()
