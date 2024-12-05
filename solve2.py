left = []
right = {}
dist=0

f = open('input.txt')
for line in f:
    elements = line.split(' ')
    left.append(int(elements[0]))
    rightval = int(elements[3])
    if rightval in right:
        right[rightval] +=1
    else:
        right[rightval] = 1


print(right)


for i in left:
    if i in right:
        dist += i * right[i]
        
    
print(dist)