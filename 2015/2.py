data=[[*map(int, i.split('x'))] for i in open('../adventofcode/2015/2.txt').read().split()]
paper=sum(map(lambda i:2*(i[0]*i[1]+i[0]*i[2]+i[1]*i[2])+min(i[0]*i[1],i[0]*i[2],i[1]*i[2]), data))
print(paper)
ribbon=sum(map(lambda i:2*min(i[0]+i[1],i[0]+i[2],i[1]+i[2])+i[0]*i[1]*i[2], data))
print(ribbon)