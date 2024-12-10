data=open('../adventofcode/2015/5.txt').read().split()
nice1=0
nice2=0
for i in data:
    if sum(i.count(n) for n in 'aeiou')>=3 and any(i[m]==i[m+1] for m in range(len(i)-1)) and sum(i.count(p) for p in ['ab','cd','pq','xy'])==0:
        nice1+=1
    a=[]
    b=[]
    for j in range(len(i)-1):
        a.append(i[j]+i[j+1])
    for k in range(len(i)-2):
        b.append(i[k]+i[k+1]+i[k+2])
    if any(a[x]==a[y] and x+1<y for x in range(len(a)-1) for y in range(len(a))) and any(z[0]==z[2] for z in b):
        nice2+=1
print(nice1)
print(nice2)