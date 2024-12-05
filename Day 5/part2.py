from collections import defaultdict, deque


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

# Codigo para la parte 2, tratamos de usar un topological sort.

def topological_sort(vertices, edges):
    # Crear un diccionario para el conteo de grados de entrada (in-degree)
    in_degree = {v: 0 for v in vertices}
    # Crear un diccionario para las adyacencias
    adjacency_list = defaultdict(list)
    
    # Poblar los diccionarios basados en las reglas (edges)
    for u, v in edges:
        adjacency_list[u].append(v)
        in_degree[v] += 1
    
    # Crear una cola con los vértices de grado de entrada 0
    queue = deque([v for v in vertices if in_degree[v] == 0])
    top_order = []

    # Realizar el ordenamiento topológico
    while queue:
        v = queue.popleft()
        top_order.append(v)
        
        # Reducir el grado de entrada de los vecinos y agregar a la cola si es 0
        for neighbor in adjacency_list[v]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return top_order

def OrderWrongOnesAndSum(orders, rules, indexes):
    sum = 0
    for count, i in enumerate(indexes):
        matchingRules = FindMatchingRulesForOrder(orders[i], rules)
        print("Sorting Index ", count, " of ",len(indexes) - 1 )
        fixed_order = topological_sort(orders[i], matchingRules)
        print(fixed_order)
        # We sum the middle value of the sorted array.
        sum += int(fixed_order[int((len(fixed_order) - 1 ) / 2)])
    print("Done, sum is: ", sum)
    return sum




lines = OpenFile(5)
print(lines)
rules = GetRules(lines)
orders = GetPagesOrder(lines)
matchingIndexs = CheckIfPageOrderIsValid(orders, rules)
#print(matchingIndexs)
wrongIndexs = [i for i in range(len(orders)) if i not in matchingIndexs] # Nos da los indexes de las ordenes incorrectas.
#print(wrongIndexs)
total = OrderWrongOnesAndSum(orders, rules, wrongIndexs)


# Obtenemos las reglas y las paginas
# Agarramos las reglas que matcheen con los numeros que tenemos en el order *tienen que tener los 2 elementos
# Revisamos que todos los elementos , cumplan con todas esas reglas
# Guardamos los correctos
# Usando los correctos creamos un array de los incorrectos.
# Los ordenamos a los incorrectos
# Encontramos el elemento del medio. array[len(array) - 1]
# Sumamos todo