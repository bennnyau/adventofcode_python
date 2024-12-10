game = open('../adventofcode/2023/7.txt').read().split('\n')
hand = [i.split()[0] for i in game]
bid = [int(i.split()[1]) for i in game]

x = list(zip(hand,bid))
label = 'A K Q J T 9 8 7 6 5 4 3 2'.split()
label2 = 'A K Q T 9 8 7 6 5 4 3 2 J'.split()
type = '5 7 9 11 13 17 25'.split()

ttw1=0
for h1,b1 in x:
    rk=1
    n1=0
    for i in label:
        n1+=(h1.count(i))**2
    for h2,b2 in x:
        n2=0
        for j in label:
            n2+=(h2.count(j))**2
        if n1 > n2:
            rk+=1
        if n1==n2:
            l1=label.index(h1[0])
            l2=label.index(h2[0])
            if l1<l2:
                rk+=1
            if l1==l2:
                l1=label.index(h1[1])
                l2=label.index(h2[1])
                if l1<l2:
                    rk+=1
                if l1==l2:
                    l1=label.index(h1[2])
                    l2=label.index(h2[2])
                    if l1<l2:
                        rk+=1
                    if l1==l2:
                        l1=label.index(h1[3])
                        l2=label.index(h2[3])
                        if l1<l2:
                            rk+=1
                        if l1==l2:
                            l1=label.index(h1[4])
                            l2=label.index(h2[4])
                            if l1<l2:
                                rk+=1
    ttw1+=b1*rk
    
ttw2=0
for h1,b1 in x:
    rk=1
    n1=0
    nj1=h1.count('J')
    for i in label:
        n1+=(h1.count(i))**2
    n1=type.index(str(n1))
    if nj1 == 1:
        if n1 in [1,2,3]:
            n1+=2
        else:
            n1+=1
    if nj1==2:
        if n1 in [1,4]:
            n1+=2
        else:
            n1+=3
    if nj1==3:
        n1+=2
    if nj1==4:
        n1+=1
    for h2,b2 in x:
        n2=0
        nj2=h2.count('J')
        for i in label:
            n2+=(h2.count(i))**2
        n2=type.index(str(n2))
        if nj2 == 1:
            if n2 in [1,2,3]:
                n2+=2
            else:
                n2+=1
        if nj2==2:
            if n2 in [1,4]:
                n2+=2
            else:
                n2+=3
        if nj2==3:
            n2+=2
        if nj2==4:
            n2+=1
        if n1 > n2:
            rk+=1
        if n1==n2:
            l1=label2.index(h1[0])
            l2=label2.index(h2[0])
            if l1<l2:
                rk+=1
            if l1==l2:
                l1=label2.index(h1[1])
                l2=label2.index(h2[1])
                if l1<l2:
                    rk+=1
                if l1==l2:
                    l1=label2.index(h1[2])
                    l2=label2.index(h2[2])
                    if l1<l2:
                        rk+=1
                    if l1==l2:
                        l1=label2.index(h1[3])
                        l2=label2.index(h2[3])
                        if l1<l2:
                            rk+=1
                        if l1==l2:
                            l1=label2.index(h1[4])
                            l2=label2.index(h2[4])
                            if l1<l2:
                                rk+=1
    ttw2+=b1*rk

print(ttw1)
print(ttw2)