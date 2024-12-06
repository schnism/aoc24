count=0

lines = open('4/input.txt').readlines()

maxx = len(lines)
maxy = len(lines[0])

def get(x,y):
    if x< maxx and y<=len(lines[x]) and x>=0 and y>=0: return lines[x][y]
    else: return '.'

for x in range(maxx):
    for y in range(maxy):
        if lines[x][y] == 'X':
            #rint(get(x-1,y),get(x-2,y),get(x-3,y))
            if get(x+1,y)=='M' and get(x+2,y)=='A' and get(x+3,y) =='S': count+=1
            if get(x-1,y)=='M' and get(x-2,y)=='A' and get(x-3,y) =='S': count+=1
            if get(x,y+1)=='M' and get(x,y+2)=='A' and get(x,y+3) =='S': count+=1
            if get(x,y-1)=='M' and get(x,y-2)=='A' and get(x,y-3) =='S': count+=1

            if get(x+1,y+1)=='M' and get(x+2,y+2)=='A' and get(x+3,y+3) =='S': count+=1
            if get(x-1,y+1)=='M' and get(x-2,y+2)=='A' and get(x-3,y+3) =='S': count+=1
            if get(x+1,y-1)=='M' and get(x+2,y-2)=='A' and get(x+3,y-3) =='S': count+=1
            if get(x-1,y-1)=='M' and get(x-2,y-2)=='A' and get(x-3,y-3) =='S': count+=1
            

print(count)