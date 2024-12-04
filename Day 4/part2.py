def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines

# Guardo la posición de las A en todo el puzzle.
# Me fijo en cada posición si la distancia alcanza para la palabra y sino no ejecuto el search.
# Me fijo si matchean con alguna de las 4 posibles combinaciones.

# M S  S S  M M  S M
#  A    A    A    A 
# M S  M M  S S  S M

def FindTheAPositions(array):
    results = []
    for y in range(0,len(array)):
        line = array[y]
        xIndexs = [i for i, c in enumerate(line) if c == "A"]
        for value in xIndexs:
            results.append((value, y))
    return results

def ScanForMatches(spotList, array):
    xLimit = len(array[0]) - 1
    yLimit = len(array) - 1
    matches = 0
    for spot in spotList:
        x, y = spot
        # Verifico que tenga espacio dentro de la grilla para que sea una opcion valida a checkear
        if(x - 1 >= 0 and x + 1 <= xLimit and y - 1 >= 0 and y + 1 <= yLimit):
            #Check for the word and sum if it matches.
            matches += CheckForWordMatch(x, y, array)
    print("Matches:",matches)

def CheckForWordMatch(x,y,array):
    #If it finds a match it will return 1 , if not 0.
    
    result = 0
    #  M S on top
    if(array[y-1][x-1] == "M" and array[y-1][x+1] == "S" and array[y+1][x-1] == "M" and array[y+1][x+1] == "S"): 
            result +=1
    # S S on top
    elif(array[y-1][x-1] == "S" and array[y-1][x+1] == "S" and array[y+1][x-1] == "M" and array[y+1][x+1] == "M"):
            result +=1
    # M M on top
    elif(array[y-1][x-1] == "M" and array[y-1][x+1] == "M" and array[y+1][x-1] == "S" and array[y+1][x+1] == "S"):
            result +=1
    # S M on top
    elif(array[y-1][x-1] == "S" and array[y-1][x+1] == "M" and array[y+1][x-1] == "S" and array[y+1][x+1] == "M"):
            result +=1
    
    return result

soup = OpenFile(4)
spotsToCheck = FindTheAPositions(soup)
#print(spotsToCheck)
ScanForMatches(spotsToCheck, soup)