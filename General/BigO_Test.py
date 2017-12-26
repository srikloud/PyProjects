
# Test Big O(N)

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

# Test Big O(N square)
print("Big O(N2)")
ll = list()
for i in range(0,1000):
    l.append(i)
for j in range(0,1000):
    ll.append(j)

print(time.time())
for k in l:
    for m in ll:
        if k == m:
            if l[k] == ll[m]:
                x = 'hello'
print(time.time())

