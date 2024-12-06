import re

sum=0

for line in open('3/input.txt'):
    for factors in re.findall(r'mul\((\d+),(\d+)\)',line):
        sum+=int(factors[0])*int(factors[1])

print(sum) # 159892596
        
