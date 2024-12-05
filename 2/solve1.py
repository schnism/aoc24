
f = open('2/input.txt')

count=0

for report in f:
    safe=True
    levels = report.split(' ')
    direction =  1 if (int(levels[0]) < int(levels[1])) else -1

    last = ''
    for level in levels:
        level=int(level)
        if last!='':
            if ((level-last)*direction>3) or ((level-last)*direction<1):
                print (level,last,direction,'unsafe')
                safe=False

        last = level
    if not(safe): print (report) 
    if safe: count+=1

print(count)
        


    