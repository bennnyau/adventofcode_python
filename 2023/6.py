from functools import reduce
from math import sqrt,floor,ceil

time, distance = open('../adventofcode/2023/6.txt').read().split('\n')
time1 = list(map(int,time.split()[1:]))
distance1 = list(map(int,distance.split()[1:]))
time2=time.split()[1:]
distance2=distance.split()[1:]

i=zip(time1,distance1)
j=zip([int(reduce(lambda x,y:x+y,time2))],[int(reduce(lambda x,y:x+y,distance2))])

def win(i):
    n=1
    for t,d in i:    
        n*=ceil((t+sqrt(t*t-4*d))/2-1)-floor((t-sqrt(t*t-4*d))/2)
    print(n)

win(i)
win(j)