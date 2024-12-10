from functools import reduce
from math import lcm

instruction, network = open('../adventofcode/2023/8.txt').read().split('\n\n')
network = network.split('\n')

a=[i[0:3] for i in network]
b=[i[7:10] for i in network]
c=[i[12:15] for i in network]
# part 1
start='AAA'
count=0
while start != 'ZZZ':
    for direction in instruction:
        if direction == 'L':
            start = b[a.index(start)]
        else:
            start = c[a.index(start)]
        count+=1
print(count)
# part 2
allnode=[i for i in a if i[2]=='A']
count=0
z=0
y=[]
e=len(allnode)
while z<e:
    for direction in instruction:
        for i in range(len(allnode)): 
            if direction == 'L':
                allnode[i] = b[a.index(allnode[i])]
            else:
                allnode[i] = c[a.index(allnode[i])]
        count+=1
        for x in allnode:
            if x[2]=='Z':
                z+=1
                allnode.remove(x)
                y.append(count)
print(reduce(lcm,y))

# GOD
import math, re

dirs, _, *graph = open("../adventofcode/2023/8.txt").read().split('\n')
# print(graph)
graph = {n: d for n, *d in [re.findall(r'\w+', s) for s in graph]}
# print(graph)
start = [n for n in graph if n.endswith('A')]

def solve(pos, i=0):
    while not pos.endswith('Z'):
        dir = dirs[i % len(dirs)]
        pos = graph[pos][dir=='R']
        i += 1
    return i

print(solve('AAA'), math.lcm(*map(solve, start)))