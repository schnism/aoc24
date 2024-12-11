import copy

map=[]
for line in open('8/input.txt').readlines():
    map.append(list(line.strip()))

maxr=len(map)
maxc=len(map[0])

antennas = copy.deepcopy(map)


for r in range(maxr):
    for c in range(maxc):
        if map[r][c] != '.':
            for r2 in range(r,maxr):
                for c2 in range(maxc):
                    if r!=r2 and c!=c2 and map[r][c] == map[r2][c2]: 
                        print ("Match ",r,c,r2,c2)
                        dr = r2-r
                        dc = c2-c
                        if c-dc>=0 and r-dr>=0 and c-dc<maxc and r-dr<maxr: antennas[r-dr][c-dc]='#'
                        if c2+dc>=0 and r2+dr>=0 and c2+dc<maxc and r2+dr<maxr: antennas[r2+dr][c2+dc]='#'
                        





'''

for line in map: print(''.join(line))
print("="*maxc)
'''

count=0
for line in antennas: 
    print(''.join(line))
    count+=line.count('#')

print(count)


