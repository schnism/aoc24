def issafe(levels):
    safe=True
    direction =  1 if (int(levels[0]) < int(levels[1])) else -1

    last = ''
    for level in levels:
        level=int(level)
        if last!='':
            if ((level-last)*direction>3) or ((level-last)*direction<1):
                safe=False

        last = level
    return safe


f = open('2/input.txt')

count=0

for report in f:
    report=report.strip()
    levels = report.split(' ')
    safe=False
    for i in range(len(levels)):
        print(i,len(levels))
        levels_damped = levels.copy()
        levels_damped.pop(i) 
        if issafe(levels_damped): safe=True
    if safe: count+=1

print(count)
