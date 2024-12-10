data = list(open('../adventofcode/2023/4.txt'))

def total_points(data):
    total=0
    for i in data:
        li1=i.partition(':')[2].partition('|')[0].strip().split(' ')
        li2=i.partition(':')[2].partition('|')[2].strip().split(' ')
        n=0
        
        for j in li1:
            for k in li2:
                if j==k and (j or k) != '':
                    n+=1
            
        if n > 0:
            total+=2**(n-1)

    print(total)

total_points(data)

def total_scratchcards(data):

    d1={}.fromkeys([i for i in range(len(data))],1)
    
    b=0
    
    for i in data:
        l1=i.partition(':')[2].partition('|')[0].strip().split(' ')
        l2=i.partition(':')[2].partition('|')[2].strip().split(' ')

        n=0
        
        for j in l1:
            for k in l2:
                if j==k and (j or k) != '':
                    n+=1
        
        if n > 0:
            d1.update({(a+b+1) : d1.get(a+b+1,0)+d1.get(b) for a in range(n)})
        
        b+=1
    print(sum(d1.values()))

total_scratchcards(data)