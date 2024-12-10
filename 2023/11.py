list=open('../adventofcode/2023/11.txt').read().splitlines()
# print(list)

di={}
n=0
for i in range(len(list)):
  for j in range(len(list[i])):
    if list[i][j] == '#':
      di|={n:(i,j)}
      n+=1

liy=[]
for i in range(len(list)):
  a=0
  for y in range(len(di)):
    if di[y][0] == i:
      a=1
      break
  if a == 0:
    liy.append(i)

lix=[]
for i in range(len(list[0])):
  a=0
  for x in range(len(di)):
    if di[x][1] == i:
      a=1
      break
  if a == 0:
    lix.append(i)
    
# print(listx)
# print(dict)
dict1={}
dict2={}
dict1|=di
dict2|=di
# part1
listy=[]
listx=[]
listy.extend(liy)
listx.extend(lix)

for i in range(len(listy)):
  for j in range(len(dict1)):
    if dict1[j][0]>=listy[i]:
      dict1[j]=(dict1[j][0]+1,dict1[j][1])
  for k in range(len(listy)):
    listy[k]+=1

for i in listx:
  for j in range(len(dict1)):
    if dict1[j][1]>=i:
      dict1[j]=(dict1[j][0],dict1[j][1]+1)
  for k in range(len(listx)):
    listx[k]+=1

dist=0

for i in range(len(dict1)):
  for j in range(i+1,len(dict1)):
    dist+=abs(dict1[i][0]-dict1[j][0])+abs(dict1[i][1]-dict1[j][1])

print(dist)

# part2
listy=[]
listx=[]
listy.extend(liy)
listx.extend(lix)

for i in range(len(listy)):
  for j in range(len(dict2)):
    if dict2[j][0]>=listy[i]:
      dict2[j]=(dict2[j][0]+999999,dict2[j][1])
  for k in range(len(listy)):
    listy[k]+=999999

for i in listx:
  for j in range(len(dict2)):
    if dict2[j][1]>=i:
      dict2[j]=(dict2[j][0],dict2[j][1]+999999)
  for k in range(len(listx)):
    listx[k]+=999999

dist=0

for i in range(len(dict2)):
  for j in range(i+1,len(dict2)):
    dist+=abs(dict2[i][0]-dict2[j][0])+abs(dict2[i][1]-dict2[j][1])

print(dist)

# GOD
xs, ys = zip(*[(x,y) for y,r in enumerate(open('../adventofcode/2023/11.txt'))
                     for x,c in enumerate(r) if c == '#'])

def dist(ps):
    ps = [sum((l, 1)[q in ps] for q in range(p)) for p in ps]
    return sum(abs(a-b) for a in ps for b in ps)//2

for l in 2, 1_000_000: print(sum(map(dist, [xs, ys])))