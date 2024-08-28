from bs4 import BeautifulSoup
import requests

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
                data = row.find_all(['th', 'td']) #tengo que buscar, en los que tiene, la clase 'data_original_value' porque sino me los da por 90 en vez del dato duro
                cell_data = [celda.get_text(strip=True) for celda in data]
                datos_posta.append(cell_data)
                

        dict_datos = []
        coso = {}
        for i in range (2, len(datos_posta) - 1):
            for j in range(0, len(datos_posta[1]) - 1):
              coso[datos_posta[1][j]] = datos_posta[i][j]
            print(coso)
            dict_datos.append(coso)

    else: 
        print(f'error en el request {res.status_code}')
    return