import re


def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines

def FindMatches(array):
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    matches = []
    for line in array:
        result = re.findall(pattern, line)
        matches.extend(result)
    return matches

def MultiplyMulValues(input):
    first = int(input.split("mul(")[1].split(",")[0])
    second = int(input.split(",")[1].split(")")[0])
    print(first, second)
    return first * second

def SumAllMuls(input):
    result = 0
    for i in input:
        result += MultiplyMulValues(i)
    return result

lines = OpenFile(3)
matches = FindMatches(lines)
result = SumAllMuls(matches)
print(result)