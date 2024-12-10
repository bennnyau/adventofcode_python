x=open('../adventofcode/2024/1.txt').read().split('\n')
# part 1
y=[]
z=[]

for i in range(len(x)):
    x[i]=[int(x[i].split('   ')[j]) for j in range(len(x[i].split('   ')))]
for i in range(len(x)):
    y.append(x[i][0])
    z.append(x[i][1])

def sortbynum(x):
    n=0
    y=[]
    for i in x:
        for j in range(len(y)):
            if i<y[j]:
                y.insert(j,i)
                n=1
                break
            elif i==y[j]:
                y.insert(j+1,i)
                n=1
                break
        if n==0:
            y.append(i)
        n=0
    return y

print(sum(abs(sortbynum(y)[i]-sortbynum(z)[i]) for i in range(len(x))))

# part 2
def simscore(x,y):
    n=0
    total=0
    for i in x:
        for j in y:
            if i==j:
                n+=1
        total+=i*n
        n=0
    return total
print(simscore(y,z))
