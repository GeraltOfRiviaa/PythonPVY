'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.80665 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.622 #? měsíční gravitace 
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu 
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu 

def earth_to_moon_weight(weight: int): 
    '''
    Calculates how much would you weight if you were on the moon 
    '''
    return (int(weight) / EARTH_GRAVITY) * MOON_GRAVITY

def km_per_hour_to_speed_of_light(km: int):
    '''
    Returns the percentage of the speed of light you entered in km/h
    i.e. if I entered 100 km/h I would be going 0.000000033% speed of light
    '''
    return 100 * (int(km) / SPEED_OF_LIGHT)

def broke_sound_barier(km: int):
    '''
    Calculates how many times did you broke the sound barier
    based on km/h
    '''
    return f"{(int(km)/SPEED_OF_SOUND)} times" if int(km) > SPEED_OF_SOUND else "0 times"
''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''