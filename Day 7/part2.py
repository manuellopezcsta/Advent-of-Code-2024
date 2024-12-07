import itertools


def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines

def GetResultsAndData(input):
    results = []
    data = []
    for line in input:
        # Get the final number
        result = int(line.split(":")[0])
        results.append(result)
        # Get the numbers for the expression
        numbers = line.split(" ")
        numbers.pop(0)
        data.append(numbers)

    return results, data

# Función para evaluar una expresión
def evalua_izquierda_a_derecha(expresion):
    tokens = expresion.split()
    result = int(tokens[0])
    
    i = 1
    while i < len(tokens) - 1:
        operador = tokens[i]
        siguiente_numero = int(tokens[i + 1])
        
        if operador == '+':
            result += siguiente_numero
        elif operador == '*':
            result *= siguiente_numero
        elif operador == '|':
            #print("ENTROOO", result, siguiente_numero , str(result) + str(siguiente_numero))
            result = int(str(result) + str(siguiente_numero))
        i += 2
        
    return result
        
def SolveAndSum(results, data):
    sum = 0
    operadores = ['+', '*',"|"]

    for i, result in enumerate(results):
        # Generar todas las combinaciones de operadores 
        #print(i)
        combinaciones_operadores = list(itertools.product(operadores, repeat=len(data[i]) - 1))

        # Probar todas las combinaciones de operadores
        for comb in combinaciones_operadores:
            expresion = f"{data[i][0]}"
            for num, op in zip(data[i][1:], comb):
                expresion += f" {op} {num}"
            #print(expresion)
            value = evalua_izquierda_a_derecha(expresion)
            #print("V: ", value)
            if value == result:
                print(f"La combinación {expresion} da como resultado {result}")
                sum += result
                break

    return sum


lines = OpenFile(7)
results, data = GetResultsAndData(lines)
sum = SolveAndSum(results, data)
print("Result: ", sum)