
import copy 
import sys

smaze = open('6/input.txt').readlines()
for i in range(len(smaze)): 
    smaze[i]=list(smaze[i].strip())
    if smaze[i].count('^')>0: 
        srow=i
        scol=smaze[i].index('^')


def ahead():
    try:    
        if dir==0 and row>0: return maze[row-1][col]
        if dir==90: return maze[row][col+1]
        if dir==180: return maze[row+1][col]
        if dir==270 and col>0: return maze[row][col-1]
    except IndexError: return 'Exit'
    return 'Exit'

def move():
    global maze
    global row
    global col
    if dir==0:
        maze[row][col]='^'
        row-=1
    if dir==90:
        maze[row][col]='>'
        col+=1
    if dir==180:
        maze[row][col]='v'
        row+=1
    if dir==270:
        maze[row][col]='<'
        col-=1



count_loops=0


for orow in range(len(smaze)):
    for ocol in range(len(smaze[orow])):

        print(orow,ocol)

        dir=0
        row=srow
        col=scol
        loop = False
        maze=copy.deepcopy(smaze)
        if not(ocol==scol and orow==srow): maze[orow][ocol]='#'


        steps=0


        while col<len(maze[0]) and col>=0 and row<len(maze) and row>=0 and not(loop):

            steps+=1

               

            if steps>50000: 
                loop=True;
                count_loops+=1
                #print(dir,ahead(),row,col)
                #for line in maze: print(''.join(line))
                #sys.exit()

            if ahead()=='#':
                dir=(dir+90)%360
            else:
                move()

            if ((
                (dir==0 or dir==180) 
                and 
                (ahead()=='^' or ahead()=='v')
                )
                or
                (
                    (dir==90 or dir==270) 
                    and 
                    (ahead()=='<' or ahead()=='>')
                )):
                loop=True
                count_loops+=1
                #print("Loop!",orow,ocol,row,col,ahead(),dir)
                #for line in maze: print(''.join(line))

print(count_loops)
