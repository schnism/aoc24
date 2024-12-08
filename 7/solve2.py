equations=[]

for line in open('7/input.txt').readlines():
    (left,right) = line.split(':')
    equations.append([int(left),[int(x) for x in right.strip().split(' ')]])

sum=0

for (target,factors) in equations:
    for oper in range(3**(len(factors)-1)):
        res=factors[0]
        sres=str(target) + ' = ' + str(factors[0])

        for i in range(len(factors)-1):

            if oper%3==0:
                res*=factors[i+1] 
                sres = sres + " * " + str(factors[i+1])
            if oper%3==1:
                res+=factors[i+1] 
                sres = sres + " + " + str(factors[i+1])
            if oper%3==2:
                res = int(str(res) + str(factors[i+1]))
                sres = sres + " || " + str(factors[i+1])

            oper=int(oper/3)

        if res==target: 
            print(sres)
            sum+=res
            break

print(sum)
