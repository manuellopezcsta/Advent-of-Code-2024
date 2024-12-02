def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines


# Take the input and make 2 lists.
# Order them
# Do n1 - n2 and abs() the result.
# Add up all the results.

def GetNumbers(input):
    list1 = []
    list2 = []
    for line in input:
       numbers = line.split()
       list1.append(int(numbers[0]))
       list2.append(int(numbers[1]))
    return list1, list2

def GetSimilarityScoreOfValue(value, list):
    #print(value, list.count(value))
    return list.count(value)

def GetSimilarityScore(list1, whereToCount):
    result = 0
    for x in range(0,len(list1)):
        result += list1[x] * GetSimilarityScoreOfValue(list1[x], whereToCount)
    return result


input = OpenFile(1)
loc1,loc2 = GetNumbers(input)
result = GetSimilarityScore(loc1, loc2)
print(result)
