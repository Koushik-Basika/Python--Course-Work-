#Built in Modules 
'''
import sys
print(sys.path)
print(sys.version)
print("start")
sys.exit()
print("end")

import platform 
print(platform.system())
print(platform.release())
print(platform.processor())

import math
print(math.pi)
print(math.e)

print(math.sqrt(36))
print(math.pow(2,3))

print(math.ceil(12.0001))
print(math.ceil(12.3))     
print(math.ceil(12.6))
print(math.ceil(12.99))

print(math.floor(12.0001))
print(math.floor(12.3))
print(math.floor(12.6))
print(math.floor(12.99))

print(math.fabs(-10))
print(math.factorial(8))
print(math.gcd(8,24))
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))


import random 
random.seed(10)
print(random.randint(1,10))
print(random.randint(20,100))
print(random.random())
print(random.uniform(1,10))

l=["R","P","S"]
print(random.choice(l))
print(random.choices(l,k=2))

random.shuffle(l)
print(l)


from collections import Counter,defaultdict,deque
s="python programming"
m="this is that that is this is is".split()
l=[1,1,1,1,2,3,4,5,45,124,12,13,1,21,32,3,4,1,32,4,5]
print(Counter(s))
print(Counter(l))
print(Counter(m))

d=defaultdict(int)
for i in s:
    d[i]+=1
print(d)  

l=deque([])
l.append(10)
l.append(20)
l.append(30)
l.popleft()                   # correct order 
l.popleft()
l.append(50)
l.append(70)
l.popleft()
print(l)


l=deque([])
l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.pop()                   # reverse order 
l.pop()
l.appendleft(50)
l.appendleft(70)
l.pop()
print(l)


from itertools import combinations,permutations 
res1=list(combinations('abc',2))
res2=list(permutations('abc',2))
print([''.join(i) for i in res1])
print([''.join(i) for i in res2])
'''




