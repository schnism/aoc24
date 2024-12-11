
compact =  [ int(x) for x in open("9/input.txt").readline().strip()]
blocks = []
id=0

for i in range(0,len(compact),2): 
    blocks.extend([id]*compact[i])
    if i+1<len(compact): blocks.extend([None]*compact[i+1])
    id+=1


for i in range(len(blocks)):
    if i%1000==0: print(i," / ",len(blocks))
    if blocks[i] == None:
        for scan in range(1,len(blocks)-i):    # Scan backwards
            if blocks[0-scan] != None:
                blocks[i]= blocks[0-scan]
                blocks[0-scan] = None
                #for c in blocks: print(c if c!=None else '.',end='')
                #print()
                break


checksum = 0
for i in range(len(blocks)):
    if blocks[i]!=None:
        checksum += i*blocks[i]

print(checksum)

