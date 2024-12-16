map = []

for line in open('10/input.txt').readlines():
    map.append([int(x) for x in list(line.strip())])


maxr = len(map)
maxc = len(map[0])

def trails(r,c,val):
    if map[r][c] != val: 
        return None
    if val==9: 
        return {(r,c)}

    result = set()
    if r>0: 
        tmp = trails(r-1,c,val+1)
        if tmp!= None: 
            for a in tmp: result.add(a)
    if c>0:
        tmp=trails(r,c-1,val+1)
        if tmp!= None: 
            for a in tmp: result.add(a)
    if r+1<maxr: 
        tmp=trails(r+1,c,val+1)
        if tmp!= None: 
            for a in tmp: result.add(a)
    if c+1<maxc: 
        tmp=trails(r,c+1,val+1)
        if tmp!= None: 
            for a in tmp: result.add(a)


    return result
    
    



count=0
for r in range(maxr):
    for c in range(maxc):
        if map[r][c]==0: 
            count+=len(trails(r,c,0))

print(count)