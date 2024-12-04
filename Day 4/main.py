def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines

# Guardo la posición de la primera letra en todo el puzzle.
# Me fijo en cada posición si la distancia alcanza para la palabra y sino no ejecuto el search.
# Me fijo si matchea la palabra, si es así sumo 1, sino sigo con la siguiente.

def FindTheXPositions(array):
    results = []
    for y in range(0,len(array)):
        line = array[y]
        xIndexs = [i for i, c in enumerate(line) if c == "X"]
        for value in xIndexs:
            results.append((value, y))
    return results

def ScanForMatches(spotList, array):
    xLimit = len(array[0]) - 1
    yLimit = len(array) - 1
    matches = 0
    for spot in spotList:
        x, y = spot
        # Las 8 direcciones posibles a escanear
        # 1 Horizontal hacia derecha
        if(x + 3 <= xLimit):
            #Check for the word and sum if it matches.
            matches += CheckForWordMatch(1, x, y, array)
        # 2 Horizontal hacia izquierda
        if(x - 3 >= 0):
            matches += CheckForWordMatch(2, x, y, array)
        # 3 Vertical hacia arriba
        if(y - 3 >= 0):
            matches += CheckForWordMatch(3, x, y, array)
        # 4 Vertical hacia abajo
        if(y + 3 <= yLimit):
            matches += CheckForWordMatch(4, x, y, array)
        # 5 Diagonal hacia arriba derecha
        if(x + 3 <= xLimit and y - 3 >= 0):
            matches += CheckForWordMatch(5, x, y, array)
        # 6 Diagonal hacia arriba izquierda
        if(x - 3 >= 0 and y - 3 >= 0):
            matches += CheckForWordMatch(6, x, y, array)
        # 7 Diagonal hacia abajo derecha
        if(x + 3 <= xLimit and y + 3 <= yLimit):
            matches += CheckForWordMatch(7, x, y, array)
        # 8 Diagonal hacia abajo izquierda
        if(x -3 >= 0 and y + 3 <= yLimit):
            matches += CheckForWordMatch(8, x, y, array)
    print("Matches:",matches)

def CheckForWordMatch(case,x,y,array):
    #If it finds a match it will return 1 , if not 0.
    # DAM U PYTHON WHY DONT U HAVE SWITCHES !
    result = 0
    if(case == 1):
        if(array[y][x+1] == "M" and array[y][x+2] == "A" and array[y][x+3] == "S"):
            result +=1
    elif(case == 2):
        if(array[y][x-1] == "M" and array[y][x-2] == "A" and array[y][x-3] == "S"):
            result +=1 
    elif(case == 3):
        if(array[y-1][x] == "M" and array[y-2][x] == "A" and array[y-3][x] == "S"):
            result +=1
    elif(case == 4):
        if(array[y+1][x] == "M" and array[y+2][x] == "A" and array[y+3][x] == "S"):
            result +=1
    elif(case == 5):
        if(array[y-1][x+1] == "M" and array[y-2][x+2] == "A" and array[y-3][x+3] == "S"):
            result +=1
    elif(case == 6):
        if(array[y-1][x-1] == "M" and array[y-2][x-2] == "A" and array[y-3][x-3] == "S"):
            result +=1
    elif(case == 7):
        if(array[y+1][x+1] == "M" and array[y+2][x+2] == "A" and array[y+3][x+3] == "S"):
            result +=1
    elif(case == 8):
        if(array[y+1][x-1] == "M" and array[y+2][x-2] == "A" and array[y+3][x-3] == "S"):
            result +=1
    return result

soup = OpenFile(4)
spotsToCheck = FindTheXPositions(soup)
#print(spotsToCheck)
ScanForMatches(spotsToCheck, soup)