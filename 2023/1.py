data = open('../adventofcode/2023/1.txt', mode='r').read()
codelist = data.splitlines()
# part 1
decodelist = []
decode=[]

y=[]

def splitstr(str, li):
    for i in str:
        li.append(i)

def reverse(li):
    for i in range(0, len(li)//2):
        temp = li[i]
        li[i] = li[-i-1]
        li[-i-1] = temp

for line in codelist:
    for letter in line:
        if letter.isnumeric():
            a=letter
            break
    splitstr(line,y)
    reverse(y)
    for letter in y:
        if letter.isnumeric():
            b=letter
            break
    decodelist.append(a+b)

for num in decodelist:
    decode.append(int(num))

print(sum(decode))
# part 2
li=[]
a=0
b=0
g=0

d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9,
     '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

for i in codelist:
    for n in range(len(i)):
        for y in d.keys():
            if i[n:].startswith(y):
                a = d.get(y)
                g=1
                break
        if g==1:
            g=0
            break
    
    for x in range(len(i)):
        for z in d.keys():
            if (i+' ')[:-x-1].endswith(z):
                b = d.get(z)
                g=1
                break
        if g==1:
            g=0
            break

    li.append(10*a+b)
print(li)

print(sum(li))
