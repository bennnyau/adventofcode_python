# part 1
data=open('../adventofcode/2015/1.txt').read()
print(data.count('(')-data.count(')'))
# part 2
n=0
for i in range(len(data)):
    if data[i]=='(':
        n+=1
    else:
        n-=1
    if n==-1:
        print(i+1)
        break