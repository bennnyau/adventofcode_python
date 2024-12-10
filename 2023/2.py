data = open('../adventofcode/2023/2.txt', mode='r').read()
# part 1
def sum_of_possible_IDs(data):
    li1 = data.splitlines()

    # example Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red

    li4=[0, 0, 0]
    total_sum=n=s=0

    for x in li1:
        n+=1
        
        li2=x.partition(':')[2].split(';')
        # print(li2)
        for y in li2:
            li4=[0, 0, 0]
            li3=y.split(',')
            # print(li3)
            # li3=[' 8 green', ' 6 blue', ' 20 red']
            for z in li3:
                if z.find('red')>=0:
                    if int(z.split(' ')[1]) > 12:
                        li4[0]=-1
                if z.find('green')>=0:
                    if int(z.split(' ')[1]) > 13:
                        li4[1]=-1            
                if z.find('blue')>=0:
                    if int(z.split(' ')[1]) > 14:
                        li4[2]=-1
            # li4=[0, 0, -1]
            # print(li4)
            if -1 in li4:
                s=1
        if s != 1:
            total_sum+=n
        else:
            s=0

    print(total_sum)

sum_of_possible_IDs(data)
# part 2
def sum_of_power(data):

    sum=0

    li1 = data.splitlines()

    # example Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red

    for x in li1:
        
        li4=[0, 0, 0]
        li2=x.partition(':')[2].split(';')
        # print(li2)
        for y in li2:
            
            li3=y.split(',')
            #print(li3)
            # li3=[' 8 green', ' 6 blue', ' 20 red']
            for z in li3:
                if z.find('red')>=0:
                    if int(z.split(' ')[1]) > li4[0]:
                        li4[0]=int(z.split(' ')[1])
                if z.find('green')>=0:
                    if int(z.split(' ')[1]) > li4[1]:
                        li4[1]=int(z.split(' ')[1])            
                if z.find('blue')>=0:
                    if int(z.split(' ')[1]) > li4[2]:
                        li4[2]=int(z.split(' ')[1])
        #print(li4)
        power = li4[0]*li4[1]*li4[2]
        sum+=power
    print(sum)

sum_of_power(data)
