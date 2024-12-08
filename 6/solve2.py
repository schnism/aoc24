
maze = open('6/input.txt').readlines()
for i in range(len(maze)): 
    maze[i]=list(maze[i].strip())
    if maze[i].count('^')>0: 
        row=i
        col=maze[i].index('^')


dir=0

def ahead():
    try:    
        if dir==0: return maze[row-1][col]
        if dir==90: return maze[row][col+1]
        if dir==180: return maze[row+1][col]
        if dir==270: return maze[row][col-1]
    except IndexError: return 'Exit'

def move():
    global maze
    global row
    global col
    maze[row][col]='X'
    if dir==0: row-=1
    if dir==90: col+=1
    if dir==180: row+=1
    if dir==270: col-=1




while col<len(maze[0]) and col>=0 and row<len(maze) and row>=0:

    if ahead()=='#':
        dir=(dir+90)%360
    else:
        move()
        
    # for line in maze: print(''.join(line))
    # print("===========================")



sum=0

for line in maze:
    for char in line:
        if char=='X': sum+=1


for line in maze: print(''.join(line))
print(sum)
