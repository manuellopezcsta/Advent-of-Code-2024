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
    print(CheckAndReturnMap(key,map), facing)
    # Puede estar vacio .
    if(CheckAndReturnMap(key,map) == "."):
        map[key] = "X"
        if(facing == 0):
            currentPos = (key[0], key[1] - 1)
        if(facing == 1):
            currentPos = (key[0] + 1, key[1])
        if(facing == 2):
            currentPos = (key[0], key[1] + 1)
        if(facing == 3):
            currentPos = (key[0] - 1, key[1])

    # Puede ser X
    if(CheckAndReturnMap(key,map) == "X"):
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

    return currentPos, facing

def GetStartingSpot(map):
    startingSpots = [k for k, v in map.items() if v == "^"]
    print("Starting spot found at: ", startingSpots[0])
    return startingSpots[0]

def SimulateGuard(map, start):
    currentPos = (start[0], start[1] - 1)
    facing = 0
    while(CheckAndReturnMap(currentPos,map) != "N"):
        print("Trying to move to " ,currentPos)
        currentPos, facing = TryToMoveHere(currentPos, map, facing)
    print("Done with the simulation")

def CountVisitedSquares(map):
    value = len([k for k, v in map.items() if v == "X"])
    return value
    

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
SimulateGuard(map, startingSpot)
visited = CountVisitedSquares(map)
print(visited)
DebugMap(map)



# Hacer el mapa
# Codigo que camine x el mapa
# Funcion de ezquinas ?
# Termina cuando sale del mapa.
# Funcion que cuente todo.