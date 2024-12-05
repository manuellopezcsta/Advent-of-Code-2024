def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines

def GetRules(array):
    rules = []
    for pair in array:
        if("|" in pair):
            x = pair.split("|")[0] 
            y = pair.split("|")[1] 
            rules.append((x,y))
        else:
            break
    #print("RULES: ", rules)
    return rules

def GetPagesOrder(array):
    book = []
    for line in array:
        if("," not in line):
            continue
        else:
            book.append(line.split(","))
    #print("BOOK: ", book)
    return book

def FindMatchingRulesForOrder(order, rules):
    matches = []
    for rule in rules:
        if(rule[0] in order and rule[1] in order):
            matches.append(rule)
        else:
            continue
    #print("Matches: ", matches)
    return matches

def CheckIfOrderFollowsRules(order, rules):
    matchingRules = FindMatchingRulesForOrder(order, rules)
    #Ver el index del elemento 1 y 2 de la regla y ver si 1 esta detras de 2.
    for rule in matchingRules:
        if(order.index(rule[0]) > order.index(rule[1])):
            return False # No cumple
        else:
            continue
    return True

def CheckIfPageOrderIsValid(orders, rules):
    result = []
    for order in orders:
        if(CheckIfOrderFollowsRules(order, rules)):
            result.append(True)
        else:
            result.append(False)
    return [i for i, val in enumerate(result) if val] # Retorna los indices del array los cuales son positivos
    #print("RESULT: ", result)

def SumTheCorrectMiddlePages(indexesArray, orders):
    sum = 0
    for index in indexesArray:
        paginas = orders[index]
        # Sumamos el valor del medio de los que son corrrectos.
        #print((len(paginas) - 1) / 2)
        sum += int(paginas[int((len(paginas) - 1 ) / 2)]) # Lo hacemos int xq es un string.
    print("SUM: ", sum)
    return sum




lines = OpenFile(5)
print(lines)
rules = GetRules(lines)
orders = GetPagesOrder(lines)
#test = FindMatchingRulesForOrder(orders[0], rules)
matchingIndexs = CheckIfPageOrderIsValid(orders, rules)
total = SumTheCorrectMiddlePages(matchingIndexs, orders)
#print(matchingIndexs)


# Obtenemos las reglas y las paginas
# Agarramos las reglas que matcheen con los numeros que tenemos en el order *tienen que tener los 2 elementos
# Revisamos que todos los elementos , cumplan con todas esas reglas
# Guardamos los correctos , y encontramos el elemento del medio. array[len(array) - 1]
# Sumamos todo