def OpenFile(dayN):
    print('Leyendo Datos')
    with open('Day ' + str(dayN) + '/input.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines

def GetReports(lines):
    reports = []
    for x in range(0,len(lines)):
        reports.append([int(x) for x in lines[x].split()])
    #print(reports)
    return reports

def CheckIfSafe(report):
    increasing = report[1] > report[0]
    safe = True
    #print("INC:",increasing)
    for x in range(0, len(report) - 1):
        if(increasing):
            if(report[x+1] - report[x] <= 3 and report[x+1] - report[x] > 0 and report[x+1] != report[x]):
                continue
            else:
                #print(report, "Unsafe")
                safe = False
                break
        else:
            if(report[x] - report[x + 1] <= 3 and report[x] - report[x + 1] > 0 and report[x+1] != report[x]):
                continue
            else:
                #print(report, "Unsafe")
                safe = False
                break
    return safe

def DoubleCheckSafety(OriginalReport):
    safe = CheckIfSafe(OriginalReport)
    if(not safe):
        for x in range(len(OriginalReport)):
            report = OriginalReport.copy()
            report.pop(x)
            safeEnough = CheckIfSafe(report)
            if(safeEnough):
                return True
            else:
                #print("Nope trying again")
                continue
        return False
    else:
        return True


lines = OpenFile(2)
reports = GetReports(lines)
#result = DoubleCheckSafety(reports[1])
#print(result)
safety = list(map(DoubleCheckSafety, reports))
print(safety)
print(safety.count(True))