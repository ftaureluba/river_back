from app.models import PlayerModel

def print_goleadores(limit=10):
    coso = PlayerModel.objects.all()
    goleadores =[]
    for cosa in coso:
        goles = 0
        for stat in cosa.stats.all():
            stats = stat.statistics
            if type(stats['goals']['total']) == int:
                goles += stats['goals']['total']
        
        goleadores.append([cosa.name, goles])
    
    goleadores.sort(key=lambda x: x[1], reverse=True)
    print(goleadores)
    return

def relevant_data():
    coso = PlayerModel.objects.all()
    