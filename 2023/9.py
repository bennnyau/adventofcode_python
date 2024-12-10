lines = open('../adventofcode/2023/9.txt').read().splitlines()
line = [line.split(' ') for line in lines]
lines1 = list(list(i)for i in (map(int,j)for j in line))
lines2 = list(list(i)for i in (map(int,reversed(j))for j in line))

def diff(x,i=0):
    z=x[-1]
    while x[-1]!=0 or x[0]!=0:
        x=[x[j+1]-x[j] for j in range(len(x)-1)]
        z+=x[-1]
    return z

print(sum(map(diff,lines1)),
      sum(map(diff,lines2)))

#GOD
data = [[*map(int, s.split())] for s in open('../adventofcode/2023/9.txt')]

def f(l):
    diffs = [b-a for a,b in zip(l, l[1:])]
    return l[-1] + f(diffs) if l else 0

for dir in 1, -1:
    print(sum(f(l[::dir]) for l in data))