data=open('../adventofcode/2015/3.txt').read()
location1=[0,0]
N=lambda x:[x[0]+1,x[1]]
E=lambda x:[x[0],x[1]+1]
S=lambda x:[x[0]-1,x[1]]
W=lambda x:[x[0],x[1]-1]
house1=[[0,0]]
def move(i,location):
    if i=='^':
        location=N(location)
    elif i=='>':
        location=E(location)
    elif i=='v':
        location=S(location)
    else:
        location=W(location)
    return(location)
for i in data:
    location1=move(i,location1)
    if location1 not in house1:
        house1.append(location1)
print(len(house1))
location1=[0,0]
location2=[0,0]
house2=[[0,0]]
for i in data[0::2]:
    location1=move(i,location1)
    if location1 not in house2:
        house2.append(location1)
for i in data[1::2]:
    location2=move(i,location2)
    if location2 not in house2:
        house2.append(location2)
print(len(house2))