from hashlib import md5
init=open('../adventofcode/2015/4.txt').read()
for i in range(10000000):
    code=md5((init+str(i)).encode()).hexdigest()
    if code[:5]=='00000':
        print(i)
        break
for i in range(10000000):
    code=md5((init+str(i)).encode()).hexdigest()
    if code[:6]=='000000':
        print(i)
        break