import re

sum=0

for line in open('3/input.txt'):
    for x in re.findall(r'mul\((\d+),(\d+)\)',line):
        sum+=int(x[0])*int(x[1])

print(sum) # 159892596
        
