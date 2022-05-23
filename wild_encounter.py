import random

def encounter_function():
    encounter_value = random.randint(1,100)
    shiny_value = random.randint(1,8192)
    global pokemon

    if encounter_value in range (1,30):
        pokemon = "snubull"
    elif encounter_value in range  (30,60):
        pokemon = "rattata"
    elif encounter_value in range  (60,80):
        pokemon = "pidgey"
    elif encounter_value in range  (80,90):
        pokemon = "abra"
    elif encounter_value in range  (90,95):
        pokemon = "jigglupyff"
    elif encounter_value in range  (95,100):
        pokemon = "jigglypuff"

    if shiny_value == (450):
        print("shiny " + pokemon)
    else:
        print(pokemon)
    
    return


steps = 0
while (steps <= 5678):
    encounter_function()
    steps += 1
