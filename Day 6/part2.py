def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines

def MakeAMap(array):
    map = {}
    for y in range(len(array)):
        for x in range(len(array[y])):
            map[(x,y)] = array[y][x]
            #print(x,y, map[(x,y)])
    return map

def CheckAndReturnMap(key,map):
    return map.get(key,"N") # We return N if there is nothing there.

def TryToMoveHere(key,map,facing):
    cause = 0
    #print(CheckAndReturnMap(key,map), facing)
    # Puede estar vacio .
    if(CheckAndReturnMap(key,map) == "."):
        map[key] = "X" + str(facing)
        if(facing == 0):
            currentPos = (key[0], key[1] - 1)
        if(facing == 1):
            currentPos = (key[0] + 1, key[1])
        if(facing == 2):
            currentPos = (key[0], key[1] + 1)
        if(facing == 3):
            currentPos = (key[0] - 1, key[1])

    # Puede ser X
    if(CheckAndReturnMap(key,map)[0] == "X"):
        if(len(CheckAndReturnMap(key,map)) == 2 and CheckAndReturnMap(key,map)[1] == facing):
            cause = 1
        if(facing == 0):
            currentPos = (key[0], key[1] - 1)
        if(facing == 1):
            currentPos = (key[0] + 1, key[1])
        if(facing == 2):
            currentPos = (key[0], key[1] + 1)
        if(facing == 3):
            currentPos = (key[0] - 1, key[1])
    
    # Puede haber una roca
    if(CheckAndReturnMap(key,map) == "#" and facing == 0):
        facing = 1
        currentPos = (key[0], key[1] + 1)
    elif(CheckAndReturnMap(key,map) == "#" and facing == 1):
        facing = 2
        currentPos = (key[0] - 1, key[1])
    elif(CheckAndReturnMap(key,map) == "#" and facing == 2):
        currentPos = (key[0], key[1] - 1)
        facing = 3
    elif(CheckAndReturnMap(key,map) == "#" and facing == 3):
        currentPos = (key[0] + 1, key[1])
        facing = 0

    # Puede estar fuera del mapa, en este caso termina.
    elif(CheckAndReturnMap(key,map) == "N"):
        print("SE SALIO DEL MAPA")
        currentPos = key
        facing = 4

    return currentPos, facing, cause

def GetStartingSpot(map):
    startingSpots = [k for k, v in map.items() if v == "^"]
    print("Starting spot found at: ", startingSpots[0])
    return startingSpots[0]

def SimulateGuard(map, start):
    currentPos = (start[0], start[1] - 1)
    facing = 0
    # It stops if it finds an N , or if it visited a block twice facing the same direction.
    while(True):
        if((len(CheckAndReturnMap(currentPos,map)) == 2 and CheckAndReturnMap(currentPos,map)[1] == str(facing))):
            #print("Loop detected")
            cause = 1
            break
        elif(CheckAndReturnMap(currentPos,map) == "N"):
            break
        else:
            currentPos, facing , cause= TryToMoveHere(currentPos, map, facing)
            # Cause will be 0 if it finished by N 
            # Or 1 if it finished by loop
    #print("Done with the simulation")
    return cause # If it works we return 0

def TryToFindLoops(map,start):
    sum = 0
    for i,item in enumerate(map.keys()):
        if(i % 100 == 0):
            print("Running Sim for ", item)
        # Para cada posicion , clonamos el mapa , y corremos el check del guardia para buscar loops . MENOS EL STARTING POINT.
        if item != start:
            newMap = map.copy()
            newMap[item] = "#"
            newMap[start] = "X0"
            sum += SimulateGuard(newMap, start)
    return sum
        



def DebugMap(map):
    mapMaxX = sorted(map.keys())[-1][0]
    mapMaxY = max(clave[1] for clave in sorted(map.keys()))
    #print(mapMaxX, mapMaxY)
    # Crear y escribir en el archivo de texto 
    with open('mapa.txt', 'w') as file:
        for y in range(mapMaxY + 1):
            line = ""
            for x in range(mapMaxX + 1):
                line += map[(x,y)]
            line += "\n"
            file.write(line)


lines = OpenFile(6)
map = MakeAMap(lines)
startingSpot = GetStartingSpot(map)
map[startingSpot] = "X"
global currentPos
global facing 
result = TryToFindLoops(map,startingSpot)
print("Loops Found: " ,result)
#SimulateGuard(map, startingSpot)
#visited = CountVisitedSquares(map)
#print(visited)
#DebugMap(map)



# PISTA

#If you've visited the same location twice and in the same direction,
#  you have a loop. So I just have a set where I add the tuple (location, direction)
#  and check I've seen it before and then abort.

# Crear una copia del mapa

# Funcion que corra la simulacion sobre todos los lugares menos el del starting Point.
# En esta funcion clono el inicial y cambio 1 lugar
# Corro la simulacion  - con nuevo check, si pasa 2 veces x un lugar break.
# Retorno true o false, y si es true sumo +1.