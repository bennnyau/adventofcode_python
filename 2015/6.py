data=[i.replace('turn off','0').replace('turn on','1').replace('toggle','2').replace('through','').split() for i in open('../adventofcode/2015/6.txt').read().split('\n')]
for i in range(len(data)):
    for j in 1,2:
        data[i][j]=[int(n) for n in data[i][j].split(',')]

lights = [[0]*1000 for j in range(1000)]
for i in data:
    for y in range(i[1][1],i[2][1]+1):
        for x in range(i[1][0],i[2][0]+1):
            if i[0]=='0':
                lights[y][x]=0
            elif i[0]=='1':
                lights[y][x]=1
            else:
                if lights[y][x]==1:
                    lights[y][x]=0
                else:
                    lights[y][x]=1
print(sum(sum(i) for i in lights))

lights = [[0]*1000 for j in range(1000)]
for i in data:
    for y in range(i[1][1],i[2][1]+1):
        for x in range(i[1][0],i[2][0]+1):
            if i[0]=='0' and lights[y][x]!=0:
                lights[y][x]-=1
            elif i[0]=='1':
                lights[y][x]+=1
            elif i[0]=='2':
                lights[y][x]+=2
print(sum(sum(i) for i in lights))