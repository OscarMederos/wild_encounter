import random

def encounterFunction():
    encounterValue = random.randint(1,100)
    shinyValue = random.randint(1,8192)
    global wildPokemon

    if encounterValue in range (1,30):
        wildPokemon = "snubull"
    elif encounterValue in range  (30,60):
        wildPokemon = "rattata"
    elif encounterValue in range  (60,80):
        wildPokemon = "pidgey"
    elif encounterValue in range  (80,90):
        wildPokemon = "abra"
    elif encounterValue in range  (90,95):
        wildPokemon = "jigglupyff"
    elif encounterValue in range  (95,100):
        wildPokemon = "ditto"

    if shinyValue == (450):
        print("shiny " + wildPokemon)
    else:
        print(wildPokemon)
    
    return


steps = 0
while (steps <= 5678):
    encounterFunction()
    steps += 1
