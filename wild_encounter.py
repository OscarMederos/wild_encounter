import random
from operator import itemgetter

# wild encounter function
def encounterFunction():
    # instantiate variables
    encounterValue = random.randint(1,100)
    shinyValue = random.randint(1,8192)
    global wildPokemon

    # return a value for wildPokemon based on the int generated by encounterValue.
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

    # add the shiny property if the shinyValue matches the static int 450.
    if shinyValue == (450):
        print("shiny " + wildPokemon.title())
    else:
        print(wildPokemon.title())
    
    return

# instantiate pokemon stats function
def instantiatePokemon():
    # create lists for the base stats, iv & ev values
    global level
    global baseHp
    global hp

    statList = random.sample(range(0, 7), 6)
    baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed = itemgetter(0, 1, 2, 3, 4, 5)(statList)

    individualValues = random.sample(range(0, 7), 6)
    hpIV, attackIV, defenseIV, spAttackIV, spDefenseIV, speedIV = itemgetter(0, 1, 2, 3, 4, 5)(individualValues)

    effortValues = random.sample(range(0, 7), 6)
    hpEV, attackEV, defenseEV, spAttackEV, spDefenseEV, speedEV = itemgetter(0, 1, 2, 3, 4, 5)(effortValues)

    # instantiate the nauture, level and floor variables
    nature = random.randint(0,24)
    level = 100
    floor = 1

    # calculate the stats
    hp = round(floor * 0.01 * (2 * baseHp + hpIV + floor * (0.25 * hpEV)) * level + level + 10)
    attack = round(floor * 0.01 * (2 * baseAttack + attackIV + floor) * (0.25 * attackEV) * level + 5 * nature)
    defense = round(floor * 0.01 * (2 * baseDefense + defenseIV + floor) * (0.25 * defenseEV) * level + 5 * nature)
    spAttack = round(floor * 0.01 * (2 * baseSpAttack + spAttackIV + floor) * (0.25 * spAttackEV) * level + 5 * nature)
    spDefense = round(floor * 0.01 * (2 * baseSpDefense + spDefenseIV + floor) * (0.25 * spDefenseEV) * level + 5 * nature)
    speed = round(floor * 0.01 * (2 * baseSpeed + speedIV + floor) * (0.25 * speedEV) * level + 5 * nature)

    print("HP: " + str(hp))
    print("Attack: " + str(attack))
    print("Defense: " + str(defense))
    print("Special Attack: " + str(spAttack))
    print("Special Defense: " + str(spDefense))
    print("Speed: " + str(speed))
    print("Nature: " + str(nature))
    #print("\n")

def catchAttempt(hp):
    status = random.randint(0,24)
    pokeBall = random.randint(0,32)
    baseHp = 50

    catchRate = 3 * baseHp - (2 * hp) * pokeBall //  (3 * baseHp) * status

    if catchRate >= 1:
        print(wildPokemon.title() + " was caught!")
        print("\n")
    else:
        print("Ah! that was close!")
        print("\n")

# simulate taking 5,678 steps in tall grass.
steps = 0
while (steps <= 8096):
    encounterFunction()
    instantiatePokemon()
    catchAttempt(hp)
    steps += 1
