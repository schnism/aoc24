count=0

lines = open('4/input.txt').readlines()

maxx = len(lines)
maxy = len(lines[0])

def get(x,y):
    if x< maxx and y<=len(lines[x]) and x>=0 and y>=0: return lines[x][y]
    else: return '.'

for x in range(maxx):
    for y in range(maxy):
        if lines[x][y] == 'A':

            if (((get(x-1,y-1)=='M' and get(x+1,y+1)=='S' ) or
             (get(x-1,y-1)=='S' and get(x+1,y+1)=='M' )) and
             ((get(x-1,y+1)=='M' and get(x+1,y-1)=='S' ) or
             (get(x-1,y+1)=='S' and get(x+1,y-1)=='M' ))):
               count+=1



print(count)