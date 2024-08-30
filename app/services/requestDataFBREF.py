from bs4 import BeautifulSoup
import requests
from app.models import PlayerModel



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
                  print(type(datos_posta[i][j]))
                else:
                  coso[datos_posta[1][j]] = datos_posta[i][j]
            
            dict_datos.append(coso)
        print(dict_datos)
        
    else: 
        print(f'error en el request {res.status_code}')
    return dict_datos


def actualizar_db(datos):
    tabla_jugadores = { #aca esta la tabla con los ids y nombres abreviados de los jugadores.
        214:	'F. Colidio',
        1201:	'E. Mammana',
        1211:	'M. Kranevitter',
        1688:	'R. Funes Mori',
        2461:	'S. Rondón',
        2463:	'F. Armani',
        2469:	'G. Pezzella',
        2473:	'M. Lanzini',
        2479:	'M. Suárez',
        2550:	'P. Díaz',
        5985:	'E. Centurión',
        5988:	'M. Casco',
        5991:	'D. Martínez',
        5995:	'N. de la Cruz',
        5997:	'I. Fernández',
        6003:	'E. Pérez',
        6008:	'B. Zuculini',
        6028:	'R. Aliendro',
        6080:	'F. Bustos',
        6237:	'E. Díaz',
        6441:	'J. Paradela',
        6492:	'C. Ledesma',
        6519:	'R. Villagra',
        6602:	'M. Herrera',
        6645:	'A. Vigo',
        9933:	'M. Borja',
        11379:	'A. Batalla',
        13402:	'A. Palavecino',
        30690:	'N. Fonseca',
        35550:	'M. Meza',
        35551:	'A. Bareiro',
        35709:	'J. Maidana',
        50875:	'L. González',
        50880:	'E. Barco',
        50886:	'G. Martínez',
        51571:	'A. Sant&apos;Anna',
        125331:	'F. Gattoni',
        125333:	'E. López',
        129992:	'T. Colletta',
        194906:	'P. Solari',
        237143:	'S. Simón',
        265971:	'L. Díaz',
        286473:	'F. Carboni',
        311316:	'F. Peña',
        311317:	'F. Londoño',
        316516:	'S. Boselli',
        404717:	'A. Encinas',
        413144:	'D. Zabala',
        413145:	'G. Trindade',
        413146:	'J. Flores',
        414329:	'A. Ruberto',
        414380:	'I. Subiabre',
        414385:	'C. Echeverri',
        414525:	'S. Beltrán',
        414526:	'L. Lavagnino',
        449249:	'F. Mastantuono',
        449510:	'T. Leiva',
        449511:	'A. González',
        455255:	'J. Luna',
        463850:	'T. Nasif',
        463851:	'L. Rivero',
        478954:	'S. Lencinas'
        }
    jugadores = PlayerModel.objects.all()
    for player in datos:
        
        jugador = PlayerModel.objects.update_or_create(

        )

    return
