map = []

for line in open('10/input.txt').readlines():
    map.append([int(x) for x in list(line.strip())])


maxr = len(map)
maxc = len(map[0])

def trails(r,c,val):
    if map[r][c] != val: 
        return 0
    if val==9: 
        return 1

    result = 0
    if r>0: 
        result+= trails(r-1,c,val+1)
    if c>0:
        result+= trails(r,c-1,val+1)
    if r+1<maxr: 
        result+= trails(r+1,c,val+1)
    if c+1<maxc: 
        result+= trails(r,c+1,val+1)

    return result
    
    



count=0
for r in range(maxr):
    for c in range(maxc):
        if map[r][c]==0: 
            count+=trails(r,c,0)

print(count)