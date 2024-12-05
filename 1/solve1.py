left = []
right = []
dist=0

f = open('input.txt')
for line in f:
    elements = line.split(' ')
    left.append(int(elements[0]))
    right.append(int(elements[3]))


right.sort()
left.sort()

for i in range(len(right)):
    dist +=  abs(right[i]-left[i])
    
print(dist)