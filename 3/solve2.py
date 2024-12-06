import re

sum=0
do=True
cleaned=''
text=''

for line in open('3/input.txt'): text+=line

for i in range(len(text)):
    if do: cleaned += text[i]
    if text[i:i+4] == 'do()': do=True
    if text[i:i+7] == 'don\'t()': do=False

for factors in re.findall(r'mul\((\d+),(\d+)\)',cleaned):
    sum+=int(factors[0])*int(factors[1])

print(sum) # 92626942
        