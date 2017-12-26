l = [1,2,3]
s = set([123])
print(s)
f = frozenset([1,2,4])
s1 = set(f)
print(s1)

s = set([1,2,3,3])
print(s)
print(s.__class__)
s1 = ([1,2,3,3])
print(s1)
print(s1.__class__)
l1 = [1,2,3]
print(l1)
print(l1.__class__)

s2 = set([])
print(s2)
s3 = set({})
print(s3)

import time
l = list()
for i in range(0,100000):
    l.append(i)
print(time.time())
for i in range(0,len(l)):
    if l[i] == 20000:
        print(l[i])
print(time.time())

print(time.time())
for i in range(0,len(l)):
    if l[i] == 30000:
        print(l[i])
print(time.time())

l = [1,2,3]
print(min(l))

