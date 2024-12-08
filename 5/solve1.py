rules= []
updates = []
sum = 0

for line in open('5/input.txt').readlines():
    if line.find('|')>0: rules.append([int(i) for i in line.split('|')])
    if line.find(',')>0: updates.append([int(i) for i in line.split(',')])

def isValid(update):
    valid=True
    for rule in rules:
        if update.count(rule[0])>0 and update.count(rule[1])>0:
            if update.index(rule[0]) > update.index(rule[1]):
                print("Rule broken: ", rule )
                valid = False
    return valid


for update in updates:
    valid = isValid(update)
    print(update, valid)
    if valid:
        sum += update[int(len(update)/2)]


print(sum)


