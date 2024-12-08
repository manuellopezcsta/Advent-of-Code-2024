def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines

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

def MakeAMap(array):
    map = {}
    for y in range(len(array)):
        for x in range(len(array[y])):
            map[(x,y)] = array[y][x]
            #print(x,y, map[(x,y)])
    return map

def CheckAndReturnMap(key,map):
    return map.get(key,"*") # We return * if there is nothing there.           

def CreateAntennaLists(map):
    # Escaneamos el mapa y guardamos en un dic nuevo como key el caracter de la antena y como entrada un array con las tuplas de donde estan.
    results = {}
    for key in map.keys():
        value = CheckAndReturnMap(key, map)
        if(value.islower() or value.isupper() or value.isdigit()):
            # We check results for if a key exists with that value.
            if(value in results):
                # If it exists, add the position to the array.
                results[value].append(key)
            else:
                # We create the entry and add the position
                results[value] = [key]
    return results

def CalculateNewPositionBasedOn2Points(point1, point2):
    newX = point2[0] + (point2[0] - point1[0])
    newY = point2[1] + (point2[1] - point1[1])
    return (newX,newY)

def CalculateVectorBetween2Points(point1, point2):
    x = (point2[0] - point1[0])
    y = (point2[1] - point1[1])
    return (x,y)


def FindAntinodes(antennas, map):
    # Get the map limits.
    mapMaxX = sorted(map.keys())[-1][0]
    mapMaxY = max(clave[1] for clave in sorted(map.keys()))
    antinodesMap = []
    # For each antenna calculate the antinodes / SKIP if its the same
    for char in antennas:
        spots = antennas[char]
        for spot in spots:
            for spot2 in spots:
                if(spot != spot2):
                    #print("Checking S1 : ", spot, " S2: ", spot2)
                    Vx,Vy = CalculateVectorBetween2Points(spot, spot2)
                    i = 0
                    antinode = CalculateNewPositionBasedOn2Points(spot, spot2)
                    while(CheckIfPointIsInsideMap(antinode, map)):
                        antinode = (antinode[0] + ( i * Vx), antinode[1] + ( i * Vy))
                        #print("Checking new spot: ", antinode)
                        i = 1
                        if(CheckIfPointIsInsideMap(antinode, map)):
                            #print("PASSED")
                            if antinode not in antinodesMap: # We only add it if its not there already to make it unique. We could use a set instead.
                                antinodesMap.append(antinode)
    # We add the antennas to the antinodes if there is more than 1.
    for antena in antennas.keys():
        if(len(antennas[antena]) > 1):
            for element in antennas[antena]:
                if element not in antinodesMap:
                    antinodesMap.append(element)
    return antinodesMap

def CheckIfPointIsInsideMap(point, map):
    if (point in map.keys()):
        return True
    else:
        return False




# Crear el mapa
# Buscar los nodos que se repitan para cada letra o numero
# Calcular los vectores entre todos esos puntos 
# Crear los antinodos si el valor para esa key existe.
# Contar los antinodos.

# Para parte 2 , tenemos que rehacer el checkeo de antidos para que siga verificando con el punto nuevo que creo si usando el vector, puede crear otro punto dentro del mapa.


lines = OpenFile(8)
map = MakeAMap(lines)
antennas = CreateAntennaLists(map)
antinodes = FindAntinodes(antennas, map)
print(len(antinodes))
#print(antinodes)
#print("ANTENNAS: ", antennas)
#print(map)